# reports.py
import os, uuid
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from db import get_db
import models, schemas

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/reports/")
async def create_report(
    type: str = Form(...),
    description: str = Form(...),
    lat: float = Form(...),
    lng: float = Form(...),
    is_anonymous: Optional[bool] = Form(False),
    files: Optional[List[UploadFile]] = File(None),
    db: Session = Depends(get_db),
):
    # 1) create report DB row
    rpt = models.Report(
        type=type,
        description=description,
        lat=lat,
        lng=lng,
        is_anonymous=is_anonymous
    )
    db.add(rpt)
    db.commit()
    db.refresh(rpt)

    # 2) save uploaded files and create media rows
    if files:
        for f in files:
            contents = await f.read()
            ext = os.path.splitext(f.filename)[1]
            unique_name = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, unique_name)
            with open(path, "wb") as out:
                out.write(contents)
            media = models.Media(
                report_id=rpt.id,
                file_name=f.filename,
                url=path,
                media_type="image" if "image" in (f.content_type or "") else "video"
            )
            db.add(media)
        db.commit()

    return {"status": "ok", "report_id": rpt.id}

@router.get("/reports/", response_model=List[schemas.ReportOut])
def list_reports(db: Session = Depends(get_db)):
    reports = db.query(models.Report).all()
    return reports

@router.get("/reports/geojson")
def reports_geojson(db: Session = Depends(get_db)):
    reports = db.query(models.Report).all()
    features = []
    for r in reports:
        features.append({
            "type": "Feature",
            "properties": {
                "id": r.id,
                "type": r.type,
                "status": r.status.value if r.status else "pending",
            },
            "geometry": {"type": "Point", "coordinates": [r.lng, r.lat]}
        })
    return {"type": "FeatureCollection", "features": features}

@router.patch("/reports/{report_id}/status")
def update_status(report_id: int, status: str = Form(...), db: Session = Depends(get_db)):
    r = db.query(models.Report).filter(models.Report.id == report_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    # validate status
    if status not in [s.value for s in models.ReportStatus]:
        raise HTTPException(status_code=400, detail="Invalid status")
    r.status = models.ReportStatus(status)
    db.add(r); db.commit(); db.refresh(r)
    return {"status": "ok", "report_id": r.id, "new_status": r.status.value}

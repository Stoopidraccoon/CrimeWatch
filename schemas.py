# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MediaOut(BaseModel):
    id: int
    file_name: str
    url: str
    media_type: str
    class Config:
        orm_mode = True

class ReportCreate(BaseModel):
    type: str
    description: str
    lat: float
    lng: float
    is_anonymous: Optional[bool] = False

class ReportOut(BaseModel):
    id: int
    type: str
    description: str
    lat: float
    lng: float
    status: str
    is_anonymous: bool
    created_at: datetime
    media: List[MediaOut] = []
    class Config:
        orm_mode = True

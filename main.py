# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
import models
from reports import router as reports_router

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Crime Reporting System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports_router)
@app.get("/")
def home():
    return {"message": "Welcome to Crime Reporting System"}


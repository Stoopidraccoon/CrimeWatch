# models.py
import enum
import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from db import Base

class ReportStatus(str, enum.Enum):
    pending = "pending"
    investigating = "investigating"
    resolved = "resolved"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120))
    email = Column(String(120), unique=True, index=True)
    password_hash = Column(String(256))
    # role omitted for now (we'll add later if needed)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(80))
    description = Column(Text)
    lat = Column(Float)
    lng = Column(Float)
    location_text = Column(String(255), nullable=True)
    time_reported = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(ReportStatus), default=ReportStatus.pending)
    is_anonymous = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    media = relationship("Media", back_populates="report", cascade="all, delete-orphan")

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(Integer, ForeignKey("reports.id"))
    file_name = Column(String(255))
    url = Column(String(512))
    media_type = Column(String(20))  # 'image' or 'video'
    report = relationship("Report", back_populates="media")

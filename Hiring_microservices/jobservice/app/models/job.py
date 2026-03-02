from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.base import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    company_id = Column(Integer, nullable=False)
    location = Column(String)
    salary = Column(String)
    job_type = Column(String) # e.g., "full-time", "contract"
    owner_email = Column(String, index=True) # The user who created the job
    created_at = Column(DateTime, default=datetime.utcnow)

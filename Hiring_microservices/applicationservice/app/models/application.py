from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.base import Base
from datetime import datetime

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, nullable=False)
    user_email = Column(String, index=True) # Identity of the applicant
    resume_url = Column(String, nullable=False)
    cover_letter = Column(String)
    status = Column(String, default="pending") # pending, accepted, rejected
    applied_at = Column(DateTime, default=datetime.utcnow)

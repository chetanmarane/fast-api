from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    employer_id = Column(Integer, ForeignKey("users.id"))
    employer = relationship("User", back_populates="jobs")
    applications = relationship("Application", back_populates="job")

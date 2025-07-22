from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from database import Base
import pytz

def current_ist():
    return datetime.now(pytz.timezone('Asia/Kolkata'))

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    # role: Mapped[str] = mapped_column(String(64), nullable=False, default="employee")
    # jobs = relationship("Job", back_populates="employer")
    # applications = relationship("Application", back_populates="employee")
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=current_ist, nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=current_ist, onupdate=current_ist)
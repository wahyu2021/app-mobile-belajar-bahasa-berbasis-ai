import datetime
from sqlalchemy import Column, String, DateTime, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    uid = Column(String(128), primary_key=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_streak_date = Column(Date)
    current_streak = Column(Integer, default=0)
    is_premium = Column(Boolean, default=False)
    
    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="user")
    leaderboard_entries = relationship("Leaderboard", back_populates="user")
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Text, DateTime
from sqlalchemy.orm import relationship
from ..database import Base

class Attempt(Base):
    __tablename__ = "attempts"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uid = Column(String(128), ForeignKey('users.uid'), nullable=False)
    level_id = Column(String(50), ForeignKey('levels.id'), nullable=False)
    score = Column(Integer, nullable=False)
    stars = Column(Integer, nullable=False)
    mistakes = Column(JSON)
    duration_seconds = Column(Integer)
    ai_feedback = Column(Text)
    completed_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="attempts")
    level = relationship("Level", back_populates="attempts")
    speech_evaluations = relationship("SpeechEvaluation", back_populates="attempt", cascade="all, delete-orphan")
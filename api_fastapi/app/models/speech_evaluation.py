from sqlalchemy import Column, Integer, ForeignKey, Float, JSON, Text
from sqlalchemy.orm import relationship
from ..database import Base

class SpeechEvaluation(Base):
    __tablename__ = "speech_evaluations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    attempt_id = Column(Integer, ForeignKey('attempts.id'), nullable=False)
    wpm = Column(Float)
    accuracy = Column(Float)
    mispronounced_tokens = Column(JSON)
    transcription = Column(Text)

    attempt = relationship("Attempt", back_populates="speech_evaluations")
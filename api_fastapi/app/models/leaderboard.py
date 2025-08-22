import datetime
from sqlalchemy import Column, String, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship
from ..database import Base

class Leaderboard(Base):
    __tablename__ = "leaderboards"
    
    season_id = Column(String(100), primary_key=True)
    user_uid = Column(String(128), ForeignKey('users.uid'), primary_key=True)
    score = Column(BigInteger, nullable=False)
    region = Column(String(100))
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="leaderboard_entries")
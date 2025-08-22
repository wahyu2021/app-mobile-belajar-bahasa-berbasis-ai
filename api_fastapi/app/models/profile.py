from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..database import Base

class Profile(Base):
    __tablename__ = "profiles"
    
    user_uid = Column(String(128), ForeignKey('users.uid'), primary_key=True)
    cefr_level_en = Column(String(10), default='A1')
    cefr_level_ja = Column(String(10), default='A1')
    interests = Column(Text)
    weakness_tags = Column(Text)

    user = relationship("User", back_populates="profile")
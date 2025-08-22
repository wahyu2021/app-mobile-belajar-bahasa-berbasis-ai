from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import level_item_association

class Level(Base):
    __tablename__ = "levels"
    
    id = Column(String(50), primary_key=True)
    world = Column(Integer, nullable=False, index=True)
    difficulty = Column(Integer, nullable=False)
    level_type = Column(String(50), nullable=False)
    objectives = Column(JSON)
    time_limit_seconds = Column(Integer)
    moves_limit = Column(Integer)
    ruleset = Column(JSON)

    items = relationship("Item", secondary=level_item_association, back_populates="levels")
    attempts = relationship("Attempt", back_populates="level")
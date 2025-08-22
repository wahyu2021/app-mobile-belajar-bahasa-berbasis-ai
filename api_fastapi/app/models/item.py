from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import level_item_association

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    language_code = Column(String(5), nullable=False)
    token_type = Column(String(50), nullable=False)
    token = Column(Text, nullable=False)
    forms = Column(JSON)
    ipa = Column(String(255))
    audio_ref = Column(String(255))
    examples = Column(JSON)

    levels = relationship("Level", secondary=level_item_association, back_populates="items")
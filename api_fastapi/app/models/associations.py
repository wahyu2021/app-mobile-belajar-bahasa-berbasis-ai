from sqlalchemy import Table, Column, String, Integer, ForeignKey
from ..database import Base

level_item_association = Table(
    'level_item_mappings', Base.metadata,
    Column('level_id', String(50), ForeignKey('levels.id'), primary_key=True),
    Column('item_id', Integer, ForeignKey('items.id'), primary_key=True)
)
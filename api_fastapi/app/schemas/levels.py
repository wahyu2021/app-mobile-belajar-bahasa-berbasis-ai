from pydantic import BaseModel
from typing import List, Dict, Any

class ItemBase(BaseModel):
    token: str
    forms: Dict[str, Any]

class LevelDetail(BaseModel):
    id: str
    world: int
    difficulty: int
    level_type: str
    objectives: Dict[str, Any]
    items_pool: List[ItemBase]

    class Config:
        from_attributes = True
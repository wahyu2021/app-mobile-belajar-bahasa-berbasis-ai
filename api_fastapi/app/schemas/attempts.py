from pydantic import BaseModel
from typing import List, Dict, Any

class MistakeDetail(BaseModel):
    token: str
    user_input: str
    target: str
    type: str

class AttemptSubmitRequest(BaseModel):
    uid: str
    level_id: str
    raw_actions: List[Dict[str, Any]]
    answers: List[str]

class AttemptSubmitResponse(BaseModel):
    score: int
    stars: int
    mistakes: List[MistakeDetail]
    ai_feedback: str
    next_hint_tags: List[str]
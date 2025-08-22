from app.schemas.attempts import AttemptSubmitRequest
from shared.ai import llm_service

async def process_attempt(attempt_data: AttemptSubmitRequest) -> dict:
    score = 3420
    stars = 3
    mistakes = [{"token": "犬", "user_input": "inu", "target": "いぬ", "type": "reading"}]
    
    ai_feedback = await llm_service.generate_narrative_feedback(mistakes)
    
    next_hint_tags = ["animals", "kana_reading"]
    
    return {
        "score": score, "stars": stars, "mistakes": mistakes,
        "ai_feedback": ai_feedback, "next_hint_tags": next_hint_tags
    }
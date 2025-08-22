from sqlalchemy.orm import Session
from ..schemas.attempts import AttemptSubmitRequest, MistakeDetail
# Impor file LLM Anda jika sudah ada
# from shared.ai import llm_service 

# Dummy LLM service untuk sekarang
class MockLLMService:
    async def generate_narrative_feedback(self, mistakes: list) -> str:
        if not mistakes:
            return "Kerja bagus! Teruslah berlatih!"
        return f"Kamu membuat {len(mistakes)} kesalahan. Terus semangat!"

llm_service = MockLLMService()

async def process_attempt(db: Session, attempt_data: AttemptSubmitRequest) -> dict:
    correct_answers = {"犬": "いぬ", "猫": "ねこ"}
    
    score = 0
    mistakes = []

    for action in attempt_data.raw_actions:
        token = action.get("token")
        user_input = action.get("userInput")
        
        if token in correct_answers and user_input == correct_answers[token]:
            score += 1000
        else:
            mistakes.append(MistakeDetail(
                token=token,
                user_input=user_input,
                target=correct_answers.get(token, "N/A"),
                type="reading"
            ))

    stars = 0
    if score > 1500: stars = 3
    elif score > 500: stars = 2
    elif score > 0: stars = 1
        
    ai_feedback = await llm_service.generate_narrative_feedback(mistakes)
    
    next_hint_tags = ["animals", "kana_reading"] if mistakes else []
    
    result = {
        "score": score,
        "stars": stars,
        "mistakes": [m.model_dump() for m in mistakes], # dump pydantic model to dict
        "ai_feedback": ai_feedback,
        "next_hint_tags": next_hint_tags
    }
    
    # Simpan hasil attempt ke DB di sini (gunakan CRUD)
    
    return result
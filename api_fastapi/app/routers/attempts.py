from fastapi import APIRouter, HTTPException
from app.schemas import attempts as schemas
from app.services import scoring_service

router = APIRouter()

@router.post("/submit", response_model=schemas.AttemptSubmitResponse)
async def submit_level_attempt(attempt_data: schemas.AttemptSubmitRequest):
    try:
        result = await scoring_service.process_attempt(attempt_data)
        validated_mistakes = [schemas.MistakeDetail(**m) for m in result.get("mistakes", [])]
        result["mistakes"] = validated_mistakes
        return schemas.AttemptSubmitResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
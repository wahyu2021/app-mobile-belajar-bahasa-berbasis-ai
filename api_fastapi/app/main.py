from fastapi import FastAPI
from app.core.config import settings
from app.routers import attempts
from shared.ai import llm_service

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
def startup_event():
    # Konfigurasi LLM saat aplikasi dimulai
    llm_service.configure_llm()

app.include_router(attempts.router, prefix=f"{settings.API_V1_STR}/attempts", tags=["Attempts"])

@app.get("/")
def root():
    return {"message": "API is running"}
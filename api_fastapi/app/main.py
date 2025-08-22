# api_fastapi/app/main.py
from fastapi import FastAPI
from .core.config import settings
from .routers import users, levels, attempts # tambahkan router lain jika ada
from .database.database import engine
from . import models

# Baris ini akan membuat tabel di DB jika belum ada
# Berguna untuk setup awal
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Sertakan semua router
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])
# app.include_router(levels.router, prefix=f"{settings.API_V1_STR}/levels", tags=["Levels"])
# app.include_router(attempts.router, prefix=f"{settings.API_V1_STR}/attempts", tags=["Attempts"])

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
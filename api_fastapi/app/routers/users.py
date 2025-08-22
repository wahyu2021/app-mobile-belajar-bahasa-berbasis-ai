from fastapi import APIRouter, Depends
from .. import models
from ..schemas import users as schemas
from ..auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    """Mengambil data profil dari pengguna yang saat ini login."""
    return current_user
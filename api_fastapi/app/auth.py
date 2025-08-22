from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import firebase_admin
from firebase_admin import auth, credentials
from sqlalchemy.orm import Session

from .database.database import get_db
from . import models
from .crud import crud_user
from .core.config import settings

try:
    cred = credentials.Certificate(settings.SERVICE_ACCOUNT_KEY_PATH)
    firebase_admin.initialize_app(cred)
    print("✅ Firebase Admin SDK berhasil diinisialisasi.")
except Exception as e:
    print(f"❌ GAGAL inisialisasi Firebase Admin SDK: {e}")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        email = decoded_token.get('email', f'{uid}@example.com')
        name = decoded_token.get('name', email.split('@')[0])

        user = crud_user.get_user(db, user_uid=uid)
        
        if not user:
            user = crud_user.create_user(db, uid=uid, email=email, name=name)

        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Gagal memvalidasi kredensial: {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )
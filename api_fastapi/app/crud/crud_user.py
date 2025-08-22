from sqlalchemy.orm import Session
from .. import models
from ..schemas import users as schemas

def get_user(db: Session, user_uid: str):
    return db.query(models.User).filter(models.User.uid == user_uid).first()

def create_user(db: Session, uid: str, email: str, name: str):
    db_user = models.User(uid=uid, email=email, name=name)
    db.add(db_user)
    db_profile = models.Profile(user_uid=uid)
    db.add(db_profile)
    db.commit()
    db.refresh(db_user)
    return db_user
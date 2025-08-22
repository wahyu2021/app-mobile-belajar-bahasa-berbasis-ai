from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None

class UserCreate(UserBase):
    uid: str

class User(UserBase):
    uid: str
    is_premium: bool

    class Config:
        from_attributes = True # Dulu orm_mode
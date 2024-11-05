from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from ..database.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole
    business_id: int
    location_id: Optional[int] = None

class UserCreateSchema(UserBase):
    pass

class UserUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    location_id: Optional[int] = None
    is_active: Optional[bool] = None

class UserSchema(UserBase):
    id: int
    is_active: bool
    google_id: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class LocationBase(BaseModel):
    name: str
    address: str
    phone: Optional[str] = None
    is_main_location: bool = False
    settings: Optional[Dict] = None
    business_id: int

class LocationCreateSchema(LocationBase):
    pass

class LocationUpdateSchema(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    is_main_location: Optional[bool] = None
    settings: Optional[Dict] = None

class LocationSchema(LocationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
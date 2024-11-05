from pydantic import BaseModel, EmailStr
from typing import Optional, Dict
from datetime import datetime
from ..database.business import BusinessType

class BusinessBase(BaseModel):
    name: str
    business_type: BusinessType
    contact_email: EmailStr
    contact_phone: Optional[str] = None
    tax_id: Optional[str] = None
    settings: Optional[Dict] = None

class BusinessCreateSchema(BusinessBase):
    pass

class BusinessUpdateSchema(BaseModel):
    name: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    contact_phone: Optional[str] = None
    settings: Optional[Dict] = None

class BusinessSchema(BusinessBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
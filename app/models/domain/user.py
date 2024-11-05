from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from ..database.user import UserRole

@dataclass
class UserDomain:
    id: int
    email: str
    full_name: str
    is_active: bool
    role: UserRole
    business_id: int
    location_id: Optional[int]
    google_id: Optional[str]
    created_at: datetime
    updated_at: datetime
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional
from ..database.business import BusinessType

@dataclass
class BusinessDomain:
    id: int
    name: str
    business_type: BusinessType
    tax_id: Optional[str]
    contact_email: str
    contact_phone: Optional[str]
    settings: Optional[Dict]
    created_at: datetime
    updated_at: datetime
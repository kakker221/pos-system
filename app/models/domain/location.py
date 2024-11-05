from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class LocationDomain:
    id: int
    name: str
    address: str
    phone: Optional[str]
    is_main_location: bool
    settings: Optional[Dict]
    business_id: int
    created_at: datetime
    updated_at: datetime

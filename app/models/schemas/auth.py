from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from app.models.database.enums import PlatformType, AuthProviderType

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    email_verified: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse
    session_id: UUID

class BaseAuthRequest(BaseModel):
    platform: PlatformType = Field(..., description="Platform type making the request")

class GoogleAuthRequest(BaseAuthRequest):
    token: str = Field(..., description="Google OAuth token")

class AppleAuthRequest(BaseAuthRequest):
    token: str = Field(..., description="Apple Sign In token")

class EmailAuthRequest(BaseAuthRequest):
    token: str = Field(..., description="Email magic link token")

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    session_id: UUID

class SessionResponse(BaseModel):
    id: UUID
    user_id: UUID
    platform: PlatformType
    is_active: bool
    last_active: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
from .service import AuthenticationService

__all__ = ["AuthenticationService"]

from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.auth import AuthResponse, TokenResponse
from app.models.database.user import User
from app.models.database.enums import PlatformType
from app.db.repositories.session import SessionRepository
from .providers import GoogleAuthProvider, AppleAuthProvider, EmailAuthProvider
from .session import SessionManager
from .token import TokenManager

class AuthenticationService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.session_repo = SessionRepository(session)
        
        self.google_provider = GoogleAuthProvider(session)
        self.apple_provider = AppleAuthProvider(session)
        self.email_provider = EmailAuthProvider(session)
        
        self.session_manager = SessionManager(session)
        self.token_manager = TokenManager()

    async def authenticate_google(self, token: str, platform: PlatformType) -> AuthResponse:
        user = await self.google_provider.authenticate(token)
        return await self._create_auth_response(user, platform)

    async def authenticate_apple(self, token: str, platform: PlatformType) -> AuthResponse:
        user = await self.apple_provider.authenticate(token)
        return await self._create_auth_response(user, platform)

    async def authenticate_email(self, token: str, platform: PlatformType) -> AuthResponse:
        user = await self.email_provider.authenticate(token)
        return await self._create_auth_response(user, platform)

    async def refresh_token(self, refresh_token: str, session_id: UUID) -> TokenResponse:
        return await self.token_manager.refresh_token(refresh_token, session_id)

    async def logout(self, session_id: UUID) -> bool:
        return await self.session_manager.deactivate_session(session_id)

    async def _create_auth_response(self, user: User, platform: PlatformType) -> AuthResponse:
        session = await self.session_manager.create_session(user.id, platform)
        tokens = self.token_manager.create_tokens(user.id, session.id)
        
        await self.session_manager.update_session_token(
            session.id, 
            tokens.refresh_token
        )
        
        return AuthResponse(
            access_token=tokens.access_token,
            refresh_token=tokens.refresh_token,
            user=user,
            session_id=session.id
        )
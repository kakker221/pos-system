from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.database.session import UserSession
from app.db.repositories.base import BaseRepository

class SessionRepository(BaseRepository[UserSession]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, UserSession)

    async def get_active_session(self, session_id: UUID) -> Optional[UserSession]:
        """Get an active session by ID"""
        query = select(self.model).where(
            self.model.id == session_id,
            self.model.is_active == True
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_user_sessions(self, user_id: UUID) -> list[UserSession]:
        """Get all sessions for a user"""
        query = select(self.model).where(
            self.model.user_id == user_id
        ).order_by(self.model.created_at.desc())
        result = await self.session.execute(query)
        return result.scalars().all()

    async def deactivate(self, session_id: UUID) -> bool:
        """Deactivate a session"""
        query = (
            update(self.model)
            .where(self.model.id == session_id)
            .values(
                is_active=False,
                updated_at=datetime.utcnow()
            )
            .returning(self.model.id)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return bool(result.scalar_one_or_none())

    async def deactivate_all_user_sessions(self, user_id: UUID) -> bool:
        """Deactivate all sessions for a user"""
        query = (
            update(self.model)
            .where(
                self.model.user_id == user_id,
                self.model.is_active == True
            )
            .values(
                is_active=False,
                updated_at=datetime.utcnow()
            )
            .returning(self.model.id)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return bool(result.scalars().first())

    async def update_last_active(self, session_id: UUID) -> Optional[UserSession]:
        """Update the last_active timestamp of a session"""
        query = (
            update(self.model)
            .where(
                self.model.id == session_id,
                self.model.is_active == True
            )
            .values(
                last_active=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            .returning(self.model)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def create(self, data: Dict[str, Any]) -> UserSession:
        """Create a new session with defaults"""
        session_data = {
            **data,
            "is_active": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        return await super().create(session_data)
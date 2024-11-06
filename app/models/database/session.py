from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint, Enum
from sqlalchemy.orm import Mapped, relationship
from .base import Base, TimestampMixin
from .user import User
from datetime import datetime, timezone
from .enums import PlatformType
from typing import Boolean

class UserSession(Base, TimestampMixin):
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    refresh_token = Column(String(1024), unique=True, nullable=False)
    device_id = Column(String(255))
    platform = Column(Enum(PlatformType))
    ip_address = Column(String(45))  # IPv6 length
    user_agent = Column(String(512))
    expires_at = Column(DateTime(timezone=True), nullable=False)
    last_used_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    user: Mapped[User] = relationship(back_populates="sessions")
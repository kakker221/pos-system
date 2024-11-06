from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint, Enum
from sqlalchemy.orm import Mapped, relationship
from .base import Base, TimestampMixin
from .enums import AuthProviderType
from .user import User

class UserAuthProvider(Base, TimestampMixin):
    __tablename__ = "user_auth_providers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider = Column(Enum(AuthProviderType), nullable=False)
    provider_user_id = Column(String(255), nullable=False)
    provider_email = Column(String(255), nullable=False)
    access_token = Column(String(1024))
    refresh_token = Column(String(1024))
    token_expires_at = Column(DateTime(timezone=True))

    user: Mapped[User] = relationship(back_populates="auth_providers")

    __table_args__ = (
        UniqueConstraint('provider', 'provider_user_id'),
    )

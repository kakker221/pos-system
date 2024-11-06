from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime

class Base(DeclarativeBase):
    """Base class for all database models"""
    pass

class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps"""
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

class UUIDMixin:
    """Mixin to add UUID primary key"""
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

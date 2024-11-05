from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin
from .enums import UserRole

class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    google_id = Column(String, unique=True)
    role = Column(Enum(UserRole), nullable=False)
    
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    business = relationship("Business", back_populates="users")
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship("Location", back_populates="users")
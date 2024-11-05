from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Location(Base, TimestampMixin):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String)
    is_main_location = Column(Boolean, default=False)
    settings = Column(JSON)
    
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    business = relationship("Business", back_populates="locations")
    users = relationship("User", back_populates="location")
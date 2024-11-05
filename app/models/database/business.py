from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin
from .enums import BusinessType

class Business(Base, TimestampMixin):
    __tablename__ = 'businesses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    business_type = Column(Enum(BusinessType), nullable=False)
    tax_id = Column(String)
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String)
    settings = Column(JSON)
    
    users = relationship("User", back_populates="business")
    locations = relationship("Location", back_populates="business")
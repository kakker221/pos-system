from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"

class BusinessType(Enum):
    RESTAURANT = "restaurant"
    CAFE = "cafe"
    BOTTLE_SHOP = "bottle_shop"
    DELI = "deli"
    FLOWER_SHOP = "flower_shop"

class AuthProviderType(str, Enum):
    GOOGLE = "google"
    APPLE = "apple"
    EMAIL = "email"

class PlatformType(str, Enum):
    WEB = "web"
    IOS = "ios"
    ANDROID = "android"

class BusinessRoleType(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"

class BusinessUserStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"
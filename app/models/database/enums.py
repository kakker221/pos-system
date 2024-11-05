import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"

class BusinessType(enum.Enum):
    RESTAURANT = "restaurant"
    CAFE = "cafe"
    BOTTLE_SHOP = "bottle_shop"
    DELI = "deli"
    FLOWER_SHOP = "flower_shop"
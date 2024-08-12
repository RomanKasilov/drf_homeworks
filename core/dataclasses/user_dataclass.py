from dataclasses import dataclass
from datetime import datetime


@dataclass
class Profile:
    id: int
    name: str
    age: int


@dataclass
class User:
    id: int
    email: str
    is_active: bool
    is_superuser: bool
    is_staff: bool
    password: str
    last_login: datetime
    created_at: datetime
    updated_at: datetime
    profile: Profile

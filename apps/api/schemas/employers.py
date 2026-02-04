from pydantic import BaseModel, validator
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str

    @validator("password")
    def strong_password(cls, v: str):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/`~" for c in v):
            raise ValueError("Password must contain at least one special character")
        return v


class UserLogin(BaseModel):
    username: str
    password: str


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: str
    phone: Optional[str]
    department: str
    designation: str
    manager: Optional[str]
    date_of_joining: date
    location: str
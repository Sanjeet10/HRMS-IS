from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    user_name: str
    password: str

    
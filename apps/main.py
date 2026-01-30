import uvicorn
from fastapi import FastAPI
from backend.schemas.employers import UserCreate
from passlib.context import CryptContext

app = FastAPI()

@app.post("/signup")
def signup(user: UserCreate):

    # Example DB save (fake)
    return {
        "username": user.user_name,
        "password_saved_as": user.password
    }

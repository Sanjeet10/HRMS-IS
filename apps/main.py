import uvicorn
from fastapi import FastAPI, HTTPException
from backend.schemas.employers import UserCreate
from passlib.context import CryptContext
from backend.core.security import hash_password

app = FastAPI()

#Fake DB for demo (replace with real DB later)
fake_users_db = {}

@app.post("/signup")
def signup(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_password
    }

    return {"message": "User created successfully"}

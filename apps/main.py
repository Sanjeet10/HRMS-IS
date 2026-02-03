import uvicorn
from fastapi import FastAPI, HTTPException
from api.schemas.employers import UserCreate, UserLogin
from passlib.context import CryptContext
from api.core.security import hash_password, verify_password

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


@app.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "username": user.username
    }
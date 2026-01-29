import uvicorn
from fastapi import FastAPI
from backend.schemas.employers import InputData

app = FastAPI()

@app.post("/employers_information")
def employer_information(data: InputData):
    return{
        "recieved": data.user_name
    }

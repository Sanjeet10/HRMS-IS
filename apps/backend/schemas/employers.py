from pydantic import BaseModel

class InputData(BaseModel):
    user_name: str
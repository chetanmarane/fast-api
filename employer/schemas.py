from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str
    employer_id: int
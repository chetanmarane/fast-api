from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str
    employer_id: int

class JobApply(BaseModel):
    job_id: int
    employee_id: int
    cover_letter: str

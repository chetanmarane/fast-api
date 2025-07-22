from pydantic import BaseModel

class JobApply(BaseModel):
    job_id: int
    employee_id: int
    cover_letter: str

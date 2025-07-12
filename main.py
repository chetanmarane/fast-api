from fastapi import FastAPI
from database import Base, engine
from routers import auth, employer, employee, job

app = FastAPI()

# Create tables
print("Registered tables:", Base.metadata.tables)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(employer.router, prefix="/employer", tags=["employer"])
app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.include_router(job.router, prefix="/job", tags=["job"])


## Removed old router-based register endpoint. All endpoints are now in routers.

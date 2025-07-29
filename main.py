from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
# from routers import auth, employer, employee, job
from user.routes import user_router
from auth.routes import auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/health", tags=["Health Checks"])
def root():
    return {"health": "True "}

# Routers
app.include_router(user_router)
app.include_router(auth_router, prefix='/api')
# app.include_router(employer.router, prefix="/employer", tags=["employer"])
# app.include_router(employee.router, prefix="/employee", tags=["employee"])
# app.include_router(job.router, prefix="/job", tags=["job"])


## Removed old router-based register endpoint. All endpoints are now in routers.

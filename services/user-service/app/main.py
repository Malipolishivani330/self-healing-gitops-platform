from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.routers.users import router as user_router
from app.database import engine
from app.models import Base

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "User Service"),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description="User Management Microservice"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to User Service",
        "environment": os.getenv("ENVIRONMENT", "development")
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
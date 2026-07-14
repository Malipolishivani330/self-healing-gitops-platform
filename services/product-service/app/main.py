from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.routers.products import router as product_router
from app.database import engine
from app.models import Base

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Product Service"),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description="Product Management Microservice"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Product Service",
        "environment": os.getenv("ENVIRONMENT", "development")
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
from fastapi import FastAPI
import models
from database import engin

app = FastAPI()

# Create all tables in the database which are defined in the models module
# The "bind=engin" argument tells SQLAlchemy to use the provided engine for creating tables
models.Base.metadata.create_all(bind=engin)

app.get("/")
async def create_database():
    return {"Database": "Created"}
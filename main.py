from fastapi import FastAPI
import models
from database import engin

app = FastAPI()

models.Base.metadata.create_all(bind=engin)

app.get("/")
async def create_database():
    return {"Database": "Created"}
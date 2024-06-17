from fastapi import FastAPI, Depends
import models
from database import engin, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create all tables in the database which are defined in the models module
# The "bind=engin" argument tells SQLAlchemy to use the provided engine for creating tables
models.Base.metadata.create_all(bind=engin)

# Function to provide a database session
def get_db():
    try:
        db = SessionLocal() # Create a new database session
        yield  db # Yield the session for use in the endpoint
    finally:
        db.close() # Ensure the session is closed after use

# Endpoint to read all todo items from the database
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    # Use the database session to query all records from the todos table
    return db.query(models.Todos).all()
from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engin

class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engin)

app = FastAPI()

# Function to provide a database session
def get_db():
    try:
        db = SessionLocal() # Create a new database session
        yield db # Yield the session for use in the endpoint
    finally:
        db.close() # Ensure the session is closed after use

def get_password_hash(password):
    return bcrypt_context.hash(password)

@app.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name

    hash_password = get_password_hash(create_user.password)
    create_user_model.hashed_password = hash_password

    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()
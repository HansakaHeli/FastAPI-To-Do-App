from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
import models
from database import engin, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from routers.auth import get_current_user, get_user_exception
from routers import auth

app = FastAPI()

# Create all tables in the database which are defined in the models module
# The "bind=engin" argument tells SQLAlchemy to use the provided engine for creating tables
models.Base.metadata.create_all(bind=engin)

app.include_router(auth.router)

# Function to provide a database session
def get_db():
    try:
        db = SessionLocal() # Create a new database session
        yield  db # Yield the session for use in the endpoint
    finally:
        db.close() # Ensure the session is closed after use

# Pydantic model for the request body
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool

# Endpoint to read all todo items from the database
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    # Use the database session to query all records from the todos table
    return db.query(models.Todos).all()

@app.get("/todos/user")
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()

# Endpoint to read a specific todo item by its ID + UserID
@app.get("/todo/{todo_id}")
async def read_todos(todo_id: int,
                     user: dict = Depends(get_current_user),
                     db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    # Endpoint to read a specific todo item by its ID
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first() # Retrieve the first result from the query
    if todo_model is not None:
        return todo_model
    # Raise an HTTP 404 Not Found exception if the todo item was not found
    raise http_exception()

# Endpoint to create a new todo item
@app.post("/")
async def create_todo(todo: Todo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    # Add the new todo item to the database session
    db.add(todo_model)
    # Commit the transaction to save the new todo item in the database
    db.commit()

    # Return a success response
    return {
        'status': 201,
        'transaction': 'Successful'
    }

# Update a todo
@app.put("/{tod_id}")
async def update_todos(todo_id: int,
                       todo: Todo,
                       user: dict = Depends(get_current_user),
                       db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()

    if todo_model is None:
        raise http_exception()

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return {
        'status': 200,
        'transaction': 'Successful'
    }

# Delete a todo
@app.delete("/{todo_id}")
async def delete_todo(todo_id: int,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()

    if todo_model is None:
        raise http_exception()

    db.query(models.Todos).filter(models.Todos == todo_id).delete()

    db.commit()

    return successful_response(200)

def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }

def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")
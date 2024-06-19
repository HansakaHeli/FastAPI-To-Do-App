from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todos", back_populates="owner")


# Define the Todos model which maps to the "todos" table in the database
class Todos(Base):

    # Specify the table name
    __tablename__ = "todos"

    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each todo item, primary ke, An index will be created for this column to speed up lookups.
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("Users", back_populates="todos")

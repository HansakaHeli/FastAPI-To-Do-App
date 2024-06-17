from sqlalchemy import Boolean, Column, Integer, String
from database import Base

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
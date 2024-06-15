from sqlalchemy import create_engine # Import the create_engine function to establish a connection to the database
from sqlalchemy.orm import sessionmaker # Import sessionmaker to create a new session
from sqlalchemy.ext.declarative import declarative_base # Import declarative_base for the base class for ORM models

# Database URL, replace with your actual database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Create a SQLAlchemy engine instance
# `connect_args={"check_same_thread": False}` is used for SQLite to allow multiple threads to interact with the database
engin = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
# autocommit=False means transactions are committed manually
# autoflush=False means the session will not flush changes to the database automatically
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

# Create a Base class for our ORM models to inherit from
Base = declarative_base()

# This is comment
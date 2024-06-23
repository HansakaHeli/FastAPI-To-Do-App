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
    phone_number = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=True)

    # Define a relationship to the Todos table, with back_populates specifying the inverse relationship
    todos = relationship("Todos", back_populates="owner")
    """
        The 'todos' attribute establishes a relationship between the Users and Todos tables.
        It allows each Users instance to have a collection of related Todos instances.

        Parameters:
        - "Todos": The related class representing the Todos table.
        - back_populates="owner": Sets up a bidirectional relationship.
          This means the Todos class will have a corresponding 'owner' attribute that links back to the Users class.
        """
    address = relationship("Address", back_populates="user_address")


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
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")
    """
        The 'owner' attribute establishes a relationship between the Todos and Users tables.
        It allows each Todos instance to be linked back to a specific Users instance.

        Parameters:
        - "Users": The related class representing the Users table.
        - back_populates="todos": Sets up a bidirectional relationship.
          This means the Users class will have a corresponding 'todos' attribute that links to the Todos class.
        """

# Address model
class Address(Base):

    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postalcode = Column(String)

    user_address = relationship("Users", back_populates="address")
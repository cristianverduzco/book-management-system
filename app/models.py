from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Book(Base):
    """
    Represents a book in the database with fields for title, author, description, and year.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=False)

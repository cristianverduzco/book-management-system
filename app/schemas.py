from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    """
    Base schema for book, defines fields for validation.
    """
    title: str
    author: str
    description: Optional[str] = None
    year: int

class BookCreate(BookBase):
    """
    Schema for creating a new book.
    """
    pass

class BookOut(BookBase):
    """
    Schema for output, includes book ID.
    """
    id: int

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to be converted to Pydantic models

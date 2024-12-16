from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session):
    """
    Retrieve all books from the database.
    """
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    """
    Retrieve a single book by its ID.
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    """
    Add a new book to the database.
    """
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

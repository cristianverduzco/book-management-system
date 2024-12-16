from fastapi import FastAPI
from .database import Base, engine
from .routers import books

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Include the books router
app.include_router(books.router, prefix="/api", tags=["books"])

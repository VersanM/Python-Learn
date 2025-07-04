from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101) # will be from 0-100

books = []


@app.get("/")
def read_api():
    return books

@app.get("/")
def get_books_by_rating(rating: int):
    result_books = []
    for book in books:
        if book.rating >= rating:
            result_books.append(book)
    return result_books

@app.post("/")
def create_book(book: Book):
    books.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in books:
        counter += 1
        if x.id == book_id:
            books[counter-1] = book
            return books[counter-1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} - Does not exist"
    )

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0

    for x in books:
        counter += 1
        if x.id == book_id:
            del books[counter-1]
            return f"ID: {book_id} was deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} - Does not exist"
    )


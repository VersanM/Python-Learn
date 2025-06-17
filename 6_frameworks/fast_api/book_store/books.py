from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

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

@app.post("/")
def create_book(book: Book):
    books.append(book)
    return book
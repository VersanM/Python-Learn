from typing import Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status
from uuid import UUID

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=-1, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Mihai Versan",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2025
            }
        }
    }

books = [
    Book(1, 'Very good book', 'Mihai Versan', 'Top description ever!', 5, 2025),
    Book(2, 'Clean Code', 'Robert C. Martin', 'This is a description of the book', 5, 2000),
    Book(3, 'Harry Potter', 'J. K. Rowling', 'No idea what description is this', 3, 2002),
    Book(4, 'Moby-Dick', 'Herman Melville', 'I am starting to run out of ideas', 4, 1972),
    Book(5, 'Don quixote', 'Miguel de Cervantes', 'Oh, wait! I have an idea', 4, 1962),
    Book(6, 'Frankestein', 'Mary Shelley', 'Actually no idea.. false alarm', 2, 1920)
]

@app.get("/books", status_code=status.HTTP_200_OK)
def read_all_books():
    return books

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(books) > 0:
        book.id = books[-1].id + 1
    else:
        book.id = 1

    return book

# get with path param
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def read_book_by_id(book_id: int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
        
# get with query param
@app.get("/books/", status_code=status.HTTP_200_OK)
def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in books:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
def read_book_by_publish_date(publish_date: int = Query(gt=0, lt=2025)):
    books_to_return = []
    for i in range(len(books)):
        if books[i].published_date == publish_date:
            books_to_return.append(books[i])
    return books_to_return

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
def update_book(book: BookRequest):
    book_change = False
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
            book_change = True
    if book_change == False:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            book_deleted = True
            break
    if book_deleted == False:
        raise HTTPException(status_code=404, detail='Item not found')
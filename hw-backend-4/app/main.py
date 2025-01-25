from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/books") #список с пагинацией
def get_books(request: Request, page: int = 1):
    per_page = 10
    books = repository.get_all()
    total_books = len(books)
    total_pages = (total_books // per_page) + (1 if total_books % per_page else 0)

    books_on_page = books[(page - 1)* per_page : page * per_page]
    return templates.TemplateResponse(
        "books/index.html",
        {"request": request, "books": books_on_page, "page": page, "total_pages": total_pages},
    )
@app.get("/books/new")  #форма добавления книги
def new_book(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})


@app.get("/books/{id}") #просмотр по id
def get_book_id(request: Request, id: int):
    book = repository.get_one(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Not found")
    return templates.TemplateResponse("books/list.html", {"request": request, "book": book})


@app.post("/books")  # Создание новой книги
def create_book(
    title: str = Form(...), 
    author: str = Form(...), 
    year: int = Form(...), 
    total_pages: int = Form(...), 
    genre: str = Form(...)
):
    # Создаём новый объект книги с ID
    new_book = {
        "id": len(repository.get_all()) + 1,  # Генерация нового ID
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre,
    }

    # Сохраняем книгу в "базу данных"
    repository.save(new_book)

    # Перенаправляем на список книг
    return RedirectResponse(url="/books", status_code=303)


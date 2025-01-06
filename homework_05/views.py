from fastapi import APIRouter, Request
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional


books = []
about_me = []

class Books(BaseModel):
    id_: int
    author: str
    name: str
    rank: Optional[int] = None

class DevInfo(BaseModel):
    name: str
    whoami: str
    info: str
    email: str

books.append(Books(id_=1, author = 'Питерс Стив', name = 'Парадокс Шимпанзе. Как управлять эмоциями для достижения своих целей'))
books.append(Books(id_=2, author = 'Келен Оливье, Блете Мари-Алис', name = 'Разработка приложений на базе GPT-4 и ChatGPT. 2-е изд.'))
books.append(Books(id_=3, author = 'Михал Плахта', name = 'Грокаем функциональное программирование', rank = 8))
books.append(Books(id_=4, author = 'Джонсон Ральф, Гамма Эрих', name = 'Паттерны объектно-ориентированного проектирования'))
books.append(Books(id_=5, author = 'Джон Галбрейт', name = 'Сетевое программирование на Python'))
books.append(Books(id_=6, author = 'Гастон Хиллар', name = 'Django RESTFul Web Services', rank = 7))


about_me.append(DevInfo(name = 'Шелудяк Антон', whoami = 'Студент группы Python Developer. Basic 2024 09', info = 'Infrastructure TeamLead, CIO, MBA, CCNP', email = 'a.shelydyak@gmail.com'))


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Список книг для чтения", 'title': 'Главная', "books": books})


@router.get("/about/", response_class=HTMLResponse)
async def about_func(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "message": "Информация обо мне", 'title': 'Информация о разработчике', "about_me": about_me})


@router.get("/api/")
async def all_books(request: Request):
    return {"books": books}


@router.get("/ping/")
async def check_ping(request: Request):
    return {"message": "pong"}


@router.get("/api/books/{id_}")
async def get_books_genre(id_: int):
    tmp = []
    for m in books:
        if m.id_ == id_:
            tmp.append(m)
    return {"books": tmp}


@router.post("/api/book/add")
async def add_book(book: Books):
    books.append(book)
    return {"Книга": book, "status": "added"}

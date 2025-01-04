
"""
Домашнее задание №5
Первое веб-приложение

- в модуле `app` создайте базовое FastAPI приложение
- создайте обычные представления
  - создайте index view `/`
  - добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике
  - создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
  - в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
  - в базовый шаблон добавьте навигационную панель `nav` (https://getbootstrap.com/docs/5.0/components/navbar/)
  - в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
  - добавьте новые зависимости в файл `requirements.txt` в корне проекта
    (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
- создайте api представления:
  - создайте api router, укажите префикс `/api`
  - добавьте вложенный роутер для вашей сущности (если не можете придумать тип сущности, рассмотрите варианты: товар, книга, автомобиль)
  - добавьте представление для чтения списка сущностей
  - добавьте представление для чтения сущности
  - добавьте представление для создания сущности
"""

from fastapi import APIRouter, Request
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


books = []


class Books(BaseModel):
    id_: int
    author: str
    name: str
    rank: Optional[int] = None

books.append(Books(id_=1, author = 'Питерс Стив', name = 'Парадокс Шимпанзе. Как управлять эмоциями для достижения своих целей'))
books.append(Books(id_=2, author = 'Келен Оливье, Блете Мари-Алис', name = 'Разработка приложений на базе GPT-4 и ChatGPT. 2-е изд.'))
books.append(Books(id_=3, author = 'Михал Плахта', name = 'Грокаем функциональное программирование', rank = 8))
books.append(Books(id_=4, author = 'Джонсон Ральф, Гамма Эрих', name = 'Паттерны объектно-ориентированного проектирования'))
books.append(Books(id_=5, author = 'Джон Галбрейт', name = 'Сетевое программирование на Python'))
books.append(Books(id_=6, author = 'Гастон Хиллар', name = 'Django RESTFul Web Services', rank = 7))


dev_info = ('''Студент группы Python Developer. Basic 2024 09
            Шелудяк Антон
            Руководитель ИТ подразделений, MBA, CCNP'''
            )


app = FastAPI()
templates = Jinja2Templates(directory="templates")


router = APIRouter(prefix='/api', tags=['Список книг для чтения'])


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Добро пожаловать!!", 'title': 'Главная', "books": books})


@app.get("/about/")
async def name_func():
    return {"message": dev_info}


@app.get("/api/")
async def all_books():
    return {"books": books}

@app.get("/books/{id_}")
async def get_books_genre(id_: int):
    tmp = []
    for m in books:
        if m.id_ == id_:
            tmp.append(m)
    return {"books": tmp}

@app.post("/api/book/add")
async def add_book(book: Books):
    books.append(book)
    return {"Книга": book, "status": "added"}

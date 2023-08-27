# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления пользователя (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel, EmailStr, SecretStr

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id_: int
    name: str
    email: EmailStr
    password: SecretStr


USERS = [User(id_=1, name='Vasya', email='1@1.ru', password='123'),
         User(id_=2, name='Petya', email='2@2.ru', password='123'),
         User(id_=3, name='Masha', email='3@3.ru', password='123')]


@app.get('/users/')
async def users():
    return {'users': USERS}


@app.post('/user/add')
async def add_user(user: User):
    USERS.append(user)
    return {"user": user, "status": "added"}


@app.put('/user/update/{user_id}')
async def update_user(user_id: int, user: User):
    for u in USERS:
        if u.id_ == user_id:
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int):
    for u in USERS:
        if u.id_ == user_id:
            USERS.remove(u)
            return {"status": "success"}
    return HTTPException(404, 'User not found')


@app.get('/all_users/', response_class=HTMLResponse)
async def all_users(request: Request):
    content = {'users': USERS,
               'request': request,
               'title': 'Пользователи',
               'page_title': 'Список пользователей'}
    return templates.TemplateResponse('read_users.html', content)


if __name__ == "__main__":
    uvicorn.run("task_3-6:app", port=8000)

# Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST
# запросы с данными нового пользователя и сохранять их в базу данных. ● Создайте модуль приложения и настройте сервер
# и маршрутизацию. ● Создайте класс User с полями id, name, email и password. ● Создайте список users для хранения
# пользователей. ● Создайте маршрут для добавления нового пользователя (метод POST). ● Реализуйте валидацию данных
# запроса и ответа.

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr, SecretStr

app = FastAPI()

USERS = []


class User(BaseModel):
    id_: int
    name: str
    email: EmailStr
    password: SecretStr


@app.get('/users/')
async def all_users():
    return {'users': USERS}


@app.post('/user/add')
async def add_user(user: User):
    USERS.append(user)
    return {"user": user, "status": "added"}


if __name__ == "__main__":
    uvicorn.run("task_3:app", port=8000)

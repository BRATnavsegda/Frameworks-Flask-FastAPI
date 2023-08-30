from typing import List
from fastapi import APIRouter

from homework_6.database import users, database
from homework_6.models import User, UserIn

user_router = APIRouter()


@user_router.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@user_router.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@user_router.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@user_router.put('/users/{user_id}', response_model=User)
async def update_user(new_user: UserIn, user_id: int):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@user_router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}

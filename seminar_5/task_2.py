# Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по заданному жанру.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Movie с полями id, title, description и genre.
# ● Создайте список movies для хранения фильмов.
# ● Создайте маршрут для получения списка фильмов по жанру (метод GET).
# ● Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = []


class Movie(BaseModel):
    id_: int
    title: str
    description: str
    genre: str


movies.append(Movie(id_=1,
                    title='The Shawshank Redemption',
                    description='Two imprisoned men bond over a number of years, finding solace and eventual '
                                'redemption through acts of common decency.',
                    genre='drama'))
movies.append(Movie(id_=2,
                    title='The Godfather',
                    description='The aging patriarch of an organized crime family transfers control of his ',
                    genre='action'))
movies.append(Movie(id_=3,
                    title='The Godfather: Part II',
                    description='The early life of ', genre='drama'))


@app.get('/movies/')
async def all_movies():
    return {'movies': movies}


@app.post('/movie/add')
async def add_movie(movie: Movie):
    movies.append(movie)
    return {"movie": movie, "status": "added"}


@app.get('/movies/{genre}')
# ● Создайте маршрут для получения списка фильмов по жанру (метод GET).
async def get_movies_by_genre(genre: str):
    tmp = []
    for m in movies:
        if m.genre == genre:
            tmp.append(m)
        if not tmp:
            raise HTTPException(404, 'Genre not found')
    return {'movies': tmp}


@app.put('/movie/update/{movie_id}')
async def update_movie(movie_id: int, movie: Movie):
    for m in movies:
        if m.id_ == movie_id:
            m.title = movie.title
            m.description = movie.description
            m.genre = movie.genre
    return {"movie": movie, "status": "updated"}


if __name__ == "__main__":
    uvicorn.run("task2:app", port=8001)

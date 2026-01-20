from fastapi import APIRouter
from fastapi.params import Depends
from app.movies.services import get_movies_from_db, get_movie_from_db, set_movie_to_db, update_movie_from_db, delete_movie_from_db
from app.database import get_session
from app.movies.schemas import MovieCreate, MovieUpdate


router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

@router.get("/")
async def get_movies(session = Depends(get_session)):
    movies = await get_movies_from_db(session)
    return movies

@router.get("/{id}")
async def get_movie(id : int, session = Depends(get_session)):
    movie = await get_movie_from_db(id, session)
    return movie

@router.post("/")
async def set_movie(movie_create : MovieCreate, session = Depends(get_session)):
    movie = await set_movie_to_db(movie_create, session)
    return movie

@router.patch("/{id}")
async def update_movie(id : int, movie_update : MovieUpdate, session = Depends(get_session)):
    movie = await update_movie_from_db(id, movie_update, session)
    return movie

@router.delete("/{id}")
async def delete_movie(id : int, session = Depends(get_session)):
    movie = await delete_movie_from_db(id, session)
    return movie
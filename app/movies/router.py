from fastapi import APIRouter
from fastapi.params import Depends
from app.movies.services import get_movies_from_db, set_movie_to_db
from app.database import get_session


router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

@router.get("/")
async def get_movies(session = Depends(get_session)):
    movies = await get_movies_from_db(session)
    return movies

@router.post("/")
async def set_movie(session = Depends(get_session)):
    movie = await set_movie_to_db(session)
    return movie
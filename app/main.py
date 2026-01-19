from fastapi import FastAPI
from app.movies.router import router as movie_router


app = FastAPI()

app.include_router(movie_router)
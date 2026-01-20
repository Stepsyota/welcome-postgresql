from pydantic import BaseModel

class MovieRead(BaseModel):
    filmname: str
    year: int | None = None
    poster: str | None = None
    rating_critics: float | None = None

class MovieCreate(BaseModel):
    filmname : str
    year : int | None = None
    poster : str | None = None
    rating_critics : float | None = None

class MovieUpdate(BaseModel):
    filmname: str | None = None
    year: int | None = None
    poster: str | None = None
    rating_critics: float | None = None
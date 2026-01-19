from pydantic import BaseModel


class MovieCreate(BaseModel):
    filmname : str
    year : int | None = None
    poster : str | None = None
    rating_critics : float | None = None
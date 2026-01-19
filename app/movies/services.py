from sqlalchemy import text
from app.movies.tables import Film

async def get_movies_from_db(session):
    result = await session.execute(text("SELECT * FROM films"))
    rows = result.mappings().all()
    list_movies = []
    for row in rows:
        list_movies.append({
            "id_film" : row['id_film'],
            "filmname" : row['filmname'],
            "year" : row['year'],
            "poster" : row['poster'],
            "rating_critics" : row['rating_critics']
        })
    return list_movies

async def set_movie_to_db(movie, session):
    orm_movie = Film(
        filmname = movie.filmname,
        year = movie.year,
        poster = movie.poster,
        rating_critics = movie.rating_critics
    )
    session.add(orm_movie)
    await session.flush() # только так появится id фильма
    return orm_movie
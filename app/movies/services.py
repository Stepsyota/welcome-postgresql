from sqlalchemy import select, text
from app.movies.tables import Film

async def get_movies_from_db(session):
    # RAW SQL
    """
    result = await session.execute(text("SELECT id_film, filmname, year, poster, rating_critics FROM films"))
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
    """
    # OR
    """
    result = await session.execute(text("SELECT id_film, filmname, year, poster, rating_critics FROM films"))
    return result.mappings().all()
    """
    # ORM
    query = select(Film)
    result = await session.execute(query)
    return result.scalars().all()


async def get_movie_from_db(id, session):
    query = select(Film).where(Film.id_film == id)
    result = await session.execute(query)
    return result.scalars().one_or_none()


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


async def update_movie_from_db(id, movie_update, session):
    query = select(Film).where(Film.id_film == id)
    result = await session.execute(query)
    movie = result.scalars().one_or_none()

    update_data = movie_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(movie, field, value)
    return movie


async def delete_movie_from_db(id, session):
    query = select(Film).where(Film.id_film == id)
    result = await session.execute(query)
    movie = result.scalars().one_or_none()
    if movie is None:
        return None

    await session.delete(movie)
    return movie
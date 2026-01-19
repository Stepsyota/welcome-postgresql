from sqlalchemy import text

async def get_movies_from_db(session):
    result = await session.execute(text("SELECT * FROM films"))
    rows = result.fetchall()
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

async def set_movie_to_db(session):
    pass
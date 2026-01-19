from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Film(Base):
    __tablename__ = "films"

    id_film = Column(Integer, primary_key=True, index=True)
    filmname = Column(String, index=True)
    year = Column(Integer, nullable=True)
    poster = Column(String, nullable=True)
    rating_critics = Column(Double, nullable=True)
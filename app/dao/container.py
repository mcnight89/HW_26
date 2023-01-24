from app.dao.directors import DirectorsDAO
from app.dao.genres import GenresDAO
from app.dao.movies import MoviesDAO
from app.database import db
from app.service.directors import DirectorsService
from app.service.genres import GenresService
from app.service.movies import MoviesService

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao)

from flask import request
from flask_restx import Resource, Namespace

from app.dao.container import genres_service
from app.dao.model.genres import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genres_service.get_all()
        return genres_schema.dump(all_genre)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid: int):
        genre = genres_service.get_one(gid)
        return genre_schema.dump(genre), 200

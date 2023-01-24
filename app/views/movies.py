from flask import request
from flask_restx import Resource, Namespace

from app.dao.container import movies_service
from app.dao.model.movies import MovieSchema, Movie
from app.database import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_req = request.args.get('director_id')
        genre_req = request.args.get('genre_id')
        year_req = request.args.get('year')

        filter = {
            "director_id":director_req,
            "genre_id":genre_req,
            "year":year_req,
        }

        all_movies = movies_service.get_all(filter)
        result = movies_schema.dump(all_movies), 200

        return result, 200

    def post(self):
        req_json = request.json
        movie = movies_service.create(req_json)

        return "done", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movies_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid

        movies_service.update(req_json)

        return "done", 204

    def delete(self, mid: int):
        movie = Movie.query.get(mid)
        db.session.delete(movie)
        db.session.commit()
        return "done", 204

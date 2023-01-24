from flask_restx import Resource, Namespace

from app.dao.container import directors_service
from app.dao.model.directors import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_director = directors_service.get_all()
        return directors_schema.dump(all_director), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did: int):
        try:
            director = directors_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception:
            return "NO", 404

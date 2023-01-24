from app.dao.directors import DirectorsDAO


class DirectorsService:
    def __init__(self, dao: DirectorsDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

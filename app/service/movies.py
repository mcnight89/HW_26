from app.dao.movies import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        if filters.get("director-id") is not None:
            movies = self.dao.get_movie_by_director(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_movie_by_genre(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_movie_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()

        return movies

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        movie = self.get_one(data.get("id"))

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        return self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)

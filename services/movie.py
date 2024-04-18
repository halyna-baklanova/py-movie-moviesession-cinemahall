from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: list = None,
    actors_ids: list = None
) -> QuerySet | Movie:
    movie_all = Movie.objects.all()

    if genres_ids:
        movie_all = movie_all.filter(genres__id__in=genres_ids)

    if actors_ids:
        movie_all = movie_all.filter(actors__id__in=actors_ids)

    return movie_all


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    movie_by_id = Movie.objects.get(id=movie_id)
    return movie_by_id


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None,
) -> Movie:
    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
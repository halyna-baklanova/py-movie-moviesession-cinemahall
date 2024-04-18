from datetime import datetime
from typing import List

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet[MovieSession]:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return movie_session


def get_movies_sessions(
        session_date: datetime = None
) -> List[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session_id = MovieSession.objects.get(id=movie_session_id)
    return movie_session_id


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session = MovieSession.objects.update(show_time=show_time)
    if movie_id:
        movie_session = MovieSession.objects.update(movie_id=movie_id)
    if cinema_hall_id:
        movie_session = MovieSession.objects.update(
            cinema_hall_id=cinema_hall_id
        )
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
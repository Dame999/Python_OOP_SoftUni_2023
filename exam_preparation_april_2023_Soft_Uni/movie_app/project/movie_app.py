from typing import List

from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def user_in_collection(self, username: str):
        if username in [u.username for u in self.users_collection if u.username == username]:
            return True
        return False

    def get_user(self, username: str):
        return [u for u in self.users_collection if u.username == username][0]

    def register_user(self, username: str, age: int):
        if self.user_in_collection(username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.user_in_collection(username):
            raise Exception("This user does not exist!")

        user = self.get_user(username)

        if movie.owner is not user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.get_user(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for attribute, value in kwargs.items():
            if attribute == 'title':
                movie.title = value
            elif attribute == 'year':
                movie.year = value
            elif attribute == 'age_restriction':
                movie.age_restriction = value
            # movie.attribute = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in [m for m in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if movie not in [m for m in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        self.movies_collection.sort(key=lambda m: (-m.year, m.title))
        # sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        return '\n'.join(m.details() for m in self.movies_collection)

    def __str__(self):
        user_usernames = [u.username for u in self.users_collection]
        movie_titles = [m.title for m in self.movies_collection]

        result = []
        if not user_usernames:
            result.append("All users: No users.")
        else:
            result.append(f"All users: {', '.join(user_usernames)}")

        if not movie_titles:
            result.append("All movies: No movies.")
        else:
            result.append(f"All movies: {', '.join(movie_titles)}")

        return '\n'.join(result)


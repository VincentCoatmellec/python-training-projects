from dataclasses import dataclass
from pathlib import Path
import json
import logging

CUR_DIR = Path(__file__).parent
DATA_FILE = CUR_DIR / "data" / "movies.json"


@dataclass
class Movie:
    title: str

    def __post_init__(self) -> None:
        """Post-initialization processing to ensure the title is properly formatted.
        """
        self.title = self.title.title()

    def __str__(self) -> str:
        return self.title

    def _get_movies(self) -> list[str]:
        """ Private method to fetch the list of movies from the JSON data file.

        Returns:
            list[str]: A list of movie titles.
        """
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies: list[str]) -> None:
        """ Private method to write the list of movies back to the JSON data file.

        Args:
            movies (list[str]): A list of movie titles to be written to the file.
        """
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)
        return None

    def add_to_movies(self) -> bool:
        """ Public method to add the movie title to the list of movies in the JSON data file. 
        It checks for duplicates before adding.

        Returns:
            bool: True if the movie was added, False otherwise.
        """
        # Fetch the current list of movies from the data file
        movies = self._get_movies()

        # Check if the movie title is already in the list to avoid duplicates
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} is already in the movies list.")
            return False

    def remove_from_movies(self) -> bool:
        """ Public method to remove the movie title from the list of movies in the JSON data file.

        Returns:
            bool: True if the movie was removed, False otherwise.
        """
        # Fetch the current list of movies from the data file
        movies = self._get_movies()

        # Check if the movie title is in the list before attempting to remove it
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} is not in the movies list.")
            return False


def get_movies() -> list[Movie]:
    with open(DATA_FILE, "r") as f:
        movies_titles = json.load(f)

    movies = [Movie(title) for title in movies_titles]
    return movies

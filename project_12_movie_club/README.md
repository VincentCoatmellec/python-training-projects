# Movie Club

A small desktop (GUI) application built with **PySide6** to manage your movie club's list of films: add, remove, and display movies, with persistent storage in a JSON file.

## Features

- Add a movie to the list (via the input field or the `Enter` key)
- Remove one or more selected movies (multi-selection supported)
- Duplicate detection on add
- Persistent storage in `data/movies.json`
- Automatic title formatting (`title case`)

## Project structure

```
project_12_movie_club/
├── app.py              # GUI interface (PySide6)
├── movie.py             # Movie model and JSON read/write logic
├── data/
│   └── movies.json      # Movie list (persistence)
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.13

## Installation

```bash
cd project_12_movie_club
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

1. Type a movie title into the text field, then click **Add Movie** (or press `Enter`).
2. Select one or more movies in the list, then click **Remove Movie** to delete them.

## Technical notes

- The `Movie` class (`movie.py`) encapsulates the movie title and the read/write operations on `data/movies.json`.
- `app.py` contains the `App` class, a PySide6 `QWidget` that displays the movie list and handles user interactions.

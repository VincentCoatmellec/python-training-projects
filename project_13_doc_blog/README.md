# 13 - Doc Blog

A small Django website built to learn the framework's fundamentals: project/app structure, URL routing, views, templates, static files, and environment-based configuration.

## Features

- Home page (`DocBlog` app) rendering a personalized greeting with the current date.
- `blog` app with:
  - an index page,
  - three article pages (`article-01`, `article-02`, `article-03`),
  - a fallback "article not found" page for any other article number.
- Static assets (CSS, background image) served through Django's staticfiles app.
- Secret key and other settings loaded from a local `.env` file via `python-dotenv`.

## Routes

| URL | View |
|---|---|
| `/` | Home page |
| `/blog/index/` | Blog index |
| `/blog/article-<number>/` | Article page (`01`, `02`, `03`, or not-found fallback) |
| `/admin/` | Django admin |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd src
cp .env.example .env
# then edit .env and set your own SECRET_KEY

python manage.py migrate
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/.

## Tech

- Python 3.13
- Django 6.1
- SQLite (default dev database, ignored by git)

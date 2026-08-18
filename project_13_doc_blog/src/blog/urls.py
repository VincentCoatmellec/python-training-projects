from django.urls import path
from .views import index, article

urlpatterns = [
    path("index/", index, name="blog-index"),
    path("article-<str:article_number>/", article, name="blog-article"),
]

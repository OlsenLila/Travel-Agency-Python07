from urllib import request
from urllib.parse import urlparse

from django.urls import path

from . import views


urlpatterns = [
    path("book_trip/", views.book_trip, name="book_trip"),
    path("popular_attraction/", views.popular_attraction, name="popular_attraction"),
]


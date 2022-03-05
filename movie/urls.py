from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popular_movies/', views.popular_movies, name='popular_movies'),
    path("movie/<int:movie_id>/", views.MovieDetail, name="moviedetail"),
]
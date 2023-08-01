from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popular_movies/', views.popular_movies, name='popular_movies'),
    path('top_rated_movies/', views.top_rated_movies, name='top_rated_movies'),
    path('upcoming_movies/', views.upcoming_movies, name='upcoming_movies'),
    path('now_playing_movies/', views.now_playing_movies, name='now_playing_movies'),
    path('trending_movies/', views.trending_movies, name='trending_movies'),
    path("movie/<int:movie_id>/", views.MovieDetail, name="moviedetail"),   
    path("recommendations/", views.SearchMovie, name="recommendations"),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
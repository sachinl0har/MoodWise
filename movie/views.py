from django.shortcuts import render
import requests


# Machine Learning Library

import csv

# Create your views here.

API_KEY = '05480c9212035931d585cd5d29ce6030'

def index(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    np_movies = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]
    top_rated_movies = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]
    upcoming_movies = requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]
    trending_movies = requests.get(f'https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}').json()['results'][:5]

    context = {'movies': movies, 'np_movies': np_movies, 'top_rated_movies': top_rated_movies, 'upcoming_movies': upcoming_movies, 'trending_movies': trending_movies,}
    return render(request, 'movie/index.html', context)

def MovieDetail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US")
    context = {"data": data.json(), "recommendations": recommendations.json(),}
    return render(request, "movie/movie_detail.html", context)

def popular_movies(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    popular_movies = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1').json()['results']
    context = {'popular_movies': popular_movies, 'movies': movies,}
    return render(request, "movie/popular_movies.html", context)

def top_rated_movies(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    top_rated_movies = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1').json()['results']
    context = {'top_rated_movies': top_rated_movies, 'movies': movies,}
    return render(request, "movie/top_rated_movies.html", context)

def upcoming_movies(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    upcoming_movies = requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=en-US&page=1').json()['results']
    context = {'upcoming_movies': upcoming_movies, 'movies': movies,}
    return render(request, "movie/upcoming_movies.html", context)

def now_playing_movies(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    now_playing_movies = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=en-US&page=1').json()['results']
    context = {'now_playing_movies': now_playing_movies, 'movies': movies,}
    return render(request, "movie/now_playing_movies.html", context)

def trending_movies(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    trending_movies = requests.get(f'https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}').json()['results']
    context = {'trending_movies': trending_movies, 'movies': movies,}
    return render(request, "movie/trending_movies.html", context)



#----------------------------------------- ALL ABOUT MACHINE LEARNING --------------------------------------------------------------------

def isMoviePresent(movie_name):
    file = open('../machine-learning/model/main_data.csv', 'r')
    reader = csv.reader(file)
    for row in reader:
        if row[18] == movie_name:
            return True
    return False

# fetch movie id from dataset and return a list
# movie_detail = [movie id, movie name]

# def getMovieDetail(movie_name):
#     try:
#         file = open('../machine-learning/model/main_data.csv', 'r')
#         reader = csv.reader(file)
#         movie_detail = []
#         for row in reader:
#             if row[18] == movie_name:
#                 movie_detail.append(row[4])
#                 movie_detail.append(movie_name)
#                 return movie_detail
#     except:
#         return movie_name
from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '05480c9212035931d585cd5d29ce6030'

def index(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    np_movies = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]
    top_rated_movies = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]
    upcoming_movies = requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=en-US&page=1').json()['results'][:5]

    context = {'movies': movies, 'np_movies': np_movies, 'top_rated_movies': top_rated_movies, 'upcoming_movies': upcoming_movies,}
    return render(request, 'movie/index.html', context)

def MovieDetail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US")
    context = {"data": data.json(), "recommendations": recommendations.json(),}
    return render(request, "movie/movie_detail.html", context)
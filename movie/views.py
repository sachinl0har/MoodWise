from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '05480c9212035931d585cd5d29ce6030'

def index(request):
    query = request.GET.get('q')
    if query:
        movies = requests.get(f'https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    else:
        return render(request, 'movie/index.html')
    context = {'movies': movies}
    return render(request, 'movie/index.html', context)

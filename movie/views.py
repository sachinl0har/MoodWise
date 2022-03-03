from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render
from numpy import empty
import requests
from django.contrib import messages 

# Create your views here.

API_KEY = '05480c9212035931d585cd5d29ce6030'

def index(request):

    without_query = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1').json()

    query = request.GET.get('q')

    movies = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}').json()
    
    # if query not in movies:
        # messages.success(request, "Please search another keyword")
        # return render(request, 'movie/index.html')
       
    # else:
    #     return render(request, 'movie/index.html')

    context = {'movies': movies, 
               'without_query': without_query}

    return render(request, 'movie/index.html', context)


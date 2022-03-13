from django.shortcuts import render
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Machine Learning Library

import csv

# Create your views here.

API_KEY = '05480c9212035931d585cd5d29ce6030'
blank_poster_url = 'https://lh3.googleusercontent.com/proxy/wEDsSXD1LTIJ1mMLGbBKQMreCPZIiPEI0EtuBHJ2PklogRVLcAX99LIJvlt25b7-kfPXD5s46UVGa8kCWZnKSmYv2rM6q9Gr9c8YgqhOsjggwMlXW_UnMH0R-hkhqHNYztnS'

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
    
    # Sachin File Location

    # file = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/movie_dataset.csv', 'r', encoding='utf-8')
    # file = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/main_data.csv', 'r', encoding='utf-8')
    
    # Harshal File Location
    file = open('D:/Django and Flask/Projects/Git Projects/MoodVice/MoodVice/MoodWise/machine-learning/model/movie_dataset.csv', 'r', encoding='utf-8')

    reader = csv.reader(file)
    for row in reader:
        if row[18] == movie_name:
            return True
    return False

# fetch movie id from dataset and return a list
# movie_detail = [movie id, movie name]
def getMovieDetail(movie_name):
    try:

        # sachin File Location
        # file = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/movie_dataset.csv', 'r', encoding='utf-8')
        
        # Harshal File Location
        file = open('D:/Django and Flask/Projects/Git Projects/MoodVice/MoodVice/MoodWise/machine-learning/model/movie_dataset.csv', 'r', encoding='utf-8')
       
        
        # file = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/main_data.csv', 'r', encoding='utf-8')
        reader = csv.reader(file)
        movie_detail = []
        for row in reader:
            if row[18] == movie_name:
                movie_detail.append(row[4])
                movie_detail.append(movie_name)
                return movie_detail
    except:
        return movie_name


# request movie detail from TMDB api and return poster url
# poster url is generated using prefix url + poster path
def getMoviePoster(movie_id):
    try:
        response = requests.get(
            'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + API_KEY + '&language=en-US')
        data = response.json()
        return 'https://image.tmdb.org/t/p/original/' + data['poster_path']
    except:
        return blank_poster_url



# searches the movie and return top 4 similar movies
def SearchMovie(request):
    searched = request.POST.get('search_box')
    
    # if movie is not in dataset return a message
    if not isMoviePresent(searched):
        return render(request, 'movie/index.html', {'message': 'Movie not found!'})

    # Reading data - set
    # f = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/movie_dataset.csv', encoding='utf-8')
    # f = open('D:/Programming/Project/Django/MoodWise/MoodWise/machine-learning/model/main_data.csv', encoding='utf-8')

    # harshal file location
    f = open('D:/Django and Flask/Projects/Git Projects/MoodVice/MoodVice/MoodWise/machine-learning/model/movie_dataset.csv', encoding='utf-8')

    df = pd.read_csv(f)

    # extracting useful features
    features = ['keywords', 'cast', 'genres', 'director']
    # features = ['comb']

    # combining the features as a single string
    def combine_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
        # return row['comb']

    # filling null entries with empty string i.e. ''
    for feature in features:
        df[feature] = df[feature].fillna('')

    # applying combined_features() method over each rows of dataframe and storing the combined string in
    # “combined_features” column
    df["combined_features"] = df.apply(combine_features, axis=1)

    cv = CountVectorizer()

    # feeding combined strings(movie contents) to CountVectorizer() object
    count_matrix = cv.fit_transform(df["combined_features"])

    # calculating cosine_similarity
    cosine_sim = cosine_similarity(count_matrix)

    # helper functions to get movie title from movie index and vice-versa.
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    def get_index_from_title(title):
        return df[df.title == title]["index"].values[0]

 

    movie_index = get_index_from_title(searched)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
    i = 0
    movie_list = []
    for element in sorted_similar_movies:
        movie_name = get_title_from_index(element[0])
        movie_detail = getMovieDetail(movie_name)
        poster = getMoviePoster(movie_detail[0])
        movie_list.append([movie_name, poster])
        i = i + 1
        if i >= 10:
            break

     # trying to add geners -- harshal

    def get_geners_from_genres(genres):
        return df[df.genres == genres]["genres"].values[0]
    
    movie_geners = get_geners_from_genres(searched)
    similar_movies_by_generes = list(enumerate(cosine_sim[movie_geners]))
    sorted_similar_movies_by_generes = sorted(similar_movies_by_generes, key=lambda x: x[1], reverse=True)[1:]


    for element in sorted_similar_movies_by_generes:
        movie_name_geners = get_title_from_index(element[0])
        movie_detail_geners = getMovieDetail(movie_name_geners)
        poster_geners = getMoviePoster(movie_detail_geners[0])
        movie_list.append([movie_name_geners, poster_geners])
        i = i + 1
        if i >= 100:
            break
        


    return render(request, 'movie/mac_learn_testing.html', {'data': movie_list})
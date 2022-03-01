import numpy as np
import pandas as pd

movies_d = pd.read_csv('../datasets/tmdb_5000_movies.csv')
credits_d = pd.read_csv('../datasets/tmdb_movies.csv')

movies_d.head()
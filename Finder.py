import requests
from urllib.parse import urlencode
import json



class Rating_search:
    def __init__(self):
        self.options = {'order': 'RATING'}
        self.headers = {'X-API-KEY': 'f7c23ff2-7657-4eda-94cf-b8fc9f83dc65'}

    def find(self, genre):
        self.options['genres'] = genre
        self.url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films' + '?' + urlencode(self.options)
        response = requests.get(self.url, headers=self.headers)
        return response.json()

class Film_data:
    def __init__(self, dct):
        local = {'TV_SERIES': 'series', 'MINI_SERIES': 'series', 'VIDEO': 'film', 'FILM': 'film', 'TV_SHOW': 'film'}
        self.kID = dct['kinopoiskId']
        if dct['nameRu'] == None:
            self.name = dct['nameOriginal']
        else:
            self.name = dct['nameRu']
        self.country = ', '.join([i['country'] for i in dct['countries']])
        self.genres = ', '.join([i['genre'] for i in dct['genres']])
        self.rating = dct['ratingKinopoisk']
        self.year = dct['year']
        self.type = local[dct['type']]
        self.poster = dct['posterUrl']


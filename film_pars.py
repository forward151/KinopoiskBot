import json
from genres import genre_dictionary
from Finder import Rating_search, Film_data

def suggest_film(file_name):
    with open(file_name, encoding='utf8') as file:
        data = json.load(file)

    fnd = Rating_search()
    genres = data['genres']
    wm = data['watched_movies']
    for i in range(len(genres)):
        gnr = genres[i]
        local_genre = genre_dictionary[gnr]
        response = fnd.find(local_genre)
        res_lst = response['items']
        for i in res_lst:
            film = Film_data(i)
            if film.kID not in wm:
                with open(file_name, 'r', encoding='utf8') as file:
                    data = json.load(file)
                data['watched_movies'].append(film.kID)
                with open(file_name, 'w') as file:
                    json.dump(data, file)
                res = [film.name, film.rating, film.year, film.genres, film.country,
                       f'https://www.kinopoisk.ru/{film.type}/{film.kID}', film.poster]
                return res
    for i in genre_dictionary:
        if i not in genres:
            local_genre = genre_dictionary[i]
            response = fnd.find(local_genre)

            res_lst = response['items']
            for i in res_lst:
                film = Film_data(i)
                if film.kID not in wm:
                    with open(file_name, 'r', encoding='utf8') as file:
                        data = json.load(file)
                    data['watched_movies'].append(film.kID)
                    with open(file_name, 'w') as file:
                        json.dump(data, file)
                    res = [film.name, film.rating, film.year, film.genres, film.country,
                           f'https://www.kinopoisk.ru/{film.type}/{film.kID}/', film.poster]
                    return res
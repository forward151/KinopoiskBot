import json


with open('User_info.json', encoding='utf8') as file:
    user_data = json.load(file)
    user_genres = user_data['genres']
    user_moves = user_data['watched_movies']
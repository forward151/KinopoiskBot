from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.model.filter_genre import FilterGenre
from kinopoisk_unofficial.model.filter_order import FilterOrder
from kinopoisk_unofficial.request.films.film_search_by_filters_request import FilmSearchByFiltersRequest

api_client = KinopoiskApiClient("f7c23ff2-7657-4eda-94cf-b8fc9f83dc65")

request = FilmSearchByFiltersRequest()
request.rating_from = 8
request.order = FilterOrder.RATING
request.add_genre(FilterGenre(1, ''))

zero_response = api_client.films.send_film_search_by_filters_request(request)
pages = zero_response.totalPages
lst = []
for i in range(pages):
    response = api_client.films.send_film_search_by_filters_request(request)
    local = response.items
    for j in local:
        if j.rating_kinopoisk is not None:
            lst.append(j)
print(lst)

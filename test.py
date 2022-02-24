import requests


url = 'https://kinopoiskapiunofficial.tech/api/v1/persons/'


headers = {'X-API-KEY': 'f7c23ff2-7657-4eda-94cf-b8fc9f83dc65'}
request = requests.get(url, headers=headers)
print(request.text)
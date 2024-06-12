import requests

import requests

API_KEY = "06f85a23d77b3a7465dd3df65f993da3"
# params = {
#     "api_key": API_KEY,
#     "query": "The Matrix",
#     "include_adult": False,
#     "language": "en-US",
#     "page": 1
#
# }
#
# response = requests.get(url, params=params)
#
# results = response.json()['results']
# print(results)

url = f"https://api.themoviedb.org/3/movie/{157336}"
params = {
    "api_key": API_KEY,
    "language": "en-US"

}
response = requests.get(url, params=params)
results = response.json()
print(results)

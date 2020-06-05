### -------------------------------- ###
# examples of API calls
### -------------------------------- ###

# website
# https://api.chucknorris.io/

# https://api.chucknorris.io/jokes/categories
# https://api.chucknorris.io/jokes/random
# https://api.chucknorris.io/jokes/random?name=Jonathan
# https://api.chucknorris.io/jokes/random?category=dev

### -------------------------------- ###
### chucklib
### -------------------------------- ###

import requests
# request library: https://requests.readthedocs.io/en/master/

# url = "https://api.chucknorris.io/jokes/random"
# response = requests.request("GET", url)
# parsed_response = response.json()

# print(parsed_response)
# print(parsed_response["value"])

def joke():
    url = "https://api.chucknorris.io/jokes/random?category=dev"
    response = requests.request("GET", url)
    parsed_response = response.json()
    return parsed_response["value"]

# import requests allows us to use public api

import requests

# from pprint import pprint sends request reponse in json format
from pprint import pprint



# var api_key equals empty string
api_key = 'b3d734cf5e18adcd52b4c7cebdce3ee5'

# var city equals input enter a city
city = input("enter the city of your choice: ")

# var base_url equals send it to a url appid= + var api_key + &q= + city
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city

# var weather_data equals requests gets base_url .json()
weather_data = requests.get(base_url).json()


#pprint weather_data
pprint(weather_data)
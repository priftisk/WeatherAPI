import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = input("City: ")

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY 

response = requests.get(URL).json()

print(response)
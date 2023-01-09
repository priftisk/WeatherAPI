import requests
import datetime as dt
import json

def kelvinToCelsius(kelvin):
    return kelvin - 273.15


API_KEY = open('api_key', 'r').read()
CITY_NAME = input("City: ")

def get_weather(city,api_key):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city} +&appid={api_key}"

    response = requests.get(URL).json()
    return response




weather_data = get_weather(CITY_NAME,API_KEY)  


print(weather_data)

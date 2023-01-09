import requests
import datetime as dt
import json
import tkinter as tk



def kelvinToCelsius(kelvin):
    return kelvin - 273.15


def get_weather(city,api_key):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city} +&appid={api_key}"

    response = requests.get(URL).json()
    return response





def main():

    API_KEY = open('api_key', 'r').read()
    CITY_NAME = input("City: ")

    weather_data = get_weather(CITY_NAME,API_KEY)  

    coord = weather_data['coord']
    weather_desc = weather_data['weather'][0]['description']
    temp_kelvin = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    city_name = weather_data['name']\
    
    window = tk.Tk()
    
    window.mainloop()



if __name__ == "__main__":
    main()

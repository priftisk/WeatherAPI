import requests
import datetime as dt
import json
import tkinter as tk



def kelvinToCelsius(kelvin):
    return round(kelvin - 273.15)


def get_weather(city,api_key):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city} +&appid={api_key}"

    response = requests.get(URL).json()
    return response

def display_city_name(city,root):
    city_label= tk.Label(root,text = f'{city}')
    city_label.config(font=('Consolas',28))
    city_label.pack(side='top')

def display_stats(temp,feels_like,humidity,root):
    temp_label = tk.Label(root,text=f'{temp} C')
    feels_like_label = tk.Label(root,text= f'Feels like {feels_like} C')
    humidity_label = tk.Label(root,text = f'{humidity}')

    temp_label.config(font=('Consolas',20))
    feels_like_label.config(font=('Consolas',20))
    humidity_label.config(font=('Consolas',20))

    temp_label.pack(side='top')
    feels_like_label.pack(side='top')
    humidity_label.pack(side='top')



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
    city_name = weather_data['name']
    
    temp_celsius = kelvinToCelsius(temp_kelvin)
    feels_like_celsius = kelvinToCelsius(feels_like)

    root = tk.Tk()
    root.geometry("300x300")
    root.title(f'{city_name} Weather')
    
    display_city_name(city_name,root)
    display_stats(temp_celsius,feels_like_celsius,humidity,root)

    root.mainloop()



if __name__ == "__main__":
    main()

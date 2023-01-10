import requests
import datetime as dt
import json
import tkinter as tk



def kelvinToCelsius(kelvin):
    return round(kelvin - 273.15)


def get_weather(canvas):
    city_name = textEntry.get()
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name} +&appid=0afee7378831f489d9d177aaf2d7556a"
    weather_data = requests.get(URL).json()
    coord = weather_data['coord']
    weather_desc = weather_data['weather'][0]['description']
    temp = int(weather_data['main']['temp']- 273.15)
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    city_name = weather_data['name']

    final_weather_data =  weather_desc + "\n" + str(temp) + "°C" 
    label1.config(text = final_weather_data)
    
    

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




canvas =tk.Tk()
canvas.geometry("500x500")
canvas.title("Current Weather Conditions")

textEntry = tk.Entry(canvas,font =('Arial',15,'bold') )
textEntry.pack(pady=20)
textEntry.focus()
textEntry.bind('<Return>', get_weather)


label1 = tk.Label(canvas, font=('Arial',15,'bold') )
label1.pack()
canvas.mainloop()



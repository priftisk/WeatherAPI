import requests
import datetime as dt
import json
import tkinter as tk
import configparser



def kelvinToCelsius(kelvin):
    return round(kelvin - 273.15)


def get_weather(canvas):
    city_name = textEntry.get()
    configParser = configparser.ConfigParser()
    configParser.read('api_key.ini')
    api_key = configParser['api']['api_key']
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name} +&appid={api_key}"
    weather_data = requests.get(URL).json()
    coord = weather_data['coord']
    weather_desc = weather_data['weather'][0]['description']
    temp = int(weather_data['main']['temp']- 273.15)
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    city_name = weather_data['name']

    final_weather_data =  "City: " + city_name + "\n" + "Desc: " + weather_desc + "\n" + "Temp: " + str(temp) + "°C" +"\n" + "Humidity: "+str(humidity) + "%"+ "\n" + "Wind speed: "+ str(wind_speed) 
    label1.config(text = final_weather_data)
    textEntry.delete(0,tk.END)
    
    

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

textEntry = tk.Entry(canvas,font =('Arial',20,'bold') )
textEntry.focus()
textEntry.bind('<Return>', get_weather)
textEntry.pack(pady=20)

sumbitButton =tk.Button()



label1 = tk.Label(canvas, font=('Arial',20,'bold') )
label1.pack()
canvas.mainloop()



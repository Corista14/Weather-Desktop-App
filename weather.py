import eel
import os
import requests

eel.init('web') # Initialize the application


def format_response(weather):
    try:
        description = weather['weather'][0]['description'].capitalize()
        temperature = weather['main']['temp']
        current_weather = f'{description}\n{temperature}°C'
    except:
        current_weather = 'Error!'
    return current_weather


@eel.expose
def get_weather(city):
    KEY = os.environ.get('weather_api_key')
    API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    api_params = {'APPID': KEY, 'q': city, 'units': 'metric'}
    response = requests.get(API_URL, params=api_params)
    weather = response.json()
    return_user = format_response(weather)
    return f'{return_user}'


eel.start('index.html', size=(450, 700))
import requests


def current_weather():
    weather = requests.get("https://api.openweathermap.org/data/2.5/weather?id=524901"
                           "&appid=aace142c57d8d83af3cdf4d68c17e04d&units=metric")
    data = weather.json()
    return data['main']['temp']


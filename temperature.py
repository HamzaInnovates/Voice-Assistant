import requests
from apikey import *
api_key = "https://api.openweathermap.org/data/2.5/weather?q=Islamabad&appid="+ temp_key
json_data = requests.get(api_key).json()
def temp():
    temprature= round(json_data["main"]["temp"]-273,1)
    return temprature
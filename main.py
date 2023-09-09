import math
import random
import requests

city = "Moscow,RU"
appid = "cb6612cc1dbf77152115c7e4e610a39a"
print('huy')
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:",city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data)
print("Минимальная температура:", data)
print("Максимальная температура", data)
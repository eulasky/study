import requests
from pprint import pprint as print

lat = 35.1729
lon = 126.8118
API_key = 'd6245335e4f8631feb550551e26789b3'
city_name = 'Gwangju, KR'

URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
data = requests.get(URL).json()
print(data)

K_TEMP = data['main']['temp']
C_TEMP = K_TEMP - 273.15
des = data['weather'][0]['description']

print(f'캘빈 온도 : {K_TEMP}K')
print(f'섭씨 온도 : {C_TEMP}')
print(f'날씨 설명: {des}')
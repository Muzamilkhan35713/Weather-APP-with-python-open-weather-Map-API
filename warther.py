import requests
API = "b3831715f3386dbf46c5251faf511a34"

name=input("Enter your city name: ")
print(name)

url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={name}&units=imperial&APPID={API}")
if(url.status_code== 404):
   print('city not found')
else:
 weather_url=url.json()
 weather_1=weather_url["weather"][0]["main"]
 temp= weather_url['main']['temp']
 humidity= weather_url['main']['humidity']
 print(f'The weather of {name}is:{weather_1}')
print(f'The temp of {name}is:{temp}')
print(f'The humidity of {name}is:{humidity}')
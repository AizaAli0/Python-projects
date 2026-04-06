import requests
import json

city = input("Enter the name of the city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=16322abc7c314a98b9782649260504&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
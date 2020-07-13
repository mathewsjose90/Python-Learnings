import requests
import json

baseurl='http://api.openweathermap.org/data/2.5/weather?'
parameters={'q':'Bangalore','appid':'bfb9b15f80ddd2a021a37aa11cd34cb1'}

response=requests.get(baseurl,params=parameters)
print(response.text)
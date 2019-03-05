# -*- coding: utf-8 -*-
import json
import requests
import sys
import credentials

# input for own city in the command line, will check if city is there
if len(sys.argv) < 1:
    print('usage: weather.py location')
    sys.exit()

# append city input to URL
location = ' '.join(sys.argv[1:])


# location = {'city': 'Seattle'}
# city = 'Seattle'
API = credentials.OWM_API


# takes response from user input and api key
URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}e&units=imperial'.format(location, API)
response = requests.get(URL)
response.raise_for_status()

# print(URL)

weatherData = json.loads(response.text)

# pulls info from API, still need to work on 'weather'
w = weatherData['main']
s = weatherData['weather']
# print(w['temp'])

# returns into requested to user
print('Current weather in {}'.format(location))
print('Temp is: ' + str(w['temp']) + '°.')
# print('Skys are ' + str(s['main']) + '.')

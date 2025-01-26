"""
File name: 7day.py
Author: JOR
Created: 09JAN25
Version: 0.1
Description: Gives a 7 day graphical forecast for one location, hard coded.
"""

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import RadioButtons
import seaborn
seaborn.set_style("darkgrid")
import requests
import json

# Buncrana': ['55.136', '-7.457']
lat='55.136'
lon='-7.457'

current_string = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,precipitation"

req = requests.get(current_string)
req = json.loads(req.text)
print(f"Latitude: {req['latitude']}")
print(f"longitude: {req['longitude']}")
print(f"Time: {req['current']['time']}")
print(f"Temperature: {req['current']['temperature_2m']} {req['current_units']['temperature_2m']}")
print(f"Wind speed: {req['current']['wind_speed_10m']} {req['current_units']['wind_speed_10m']}")
print(f"Precipitation: {req['current']['precipitation']} {req['current_units']['precipitation']}")

forecast_string = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,wind_speed_10m,precipitation"
req = requests.get(forecast_string)
req = json.loads(req.text)

times = req['hourly']['time']
times[:] = [s[:10] + "   " + s[11:] for s in times]

temperatures = req['hourly']['temperature_2m']
wind = req['hourly']['wind_speed_10m']
precipitation = req['hourly']['precipitation']
plt.plot(times, temperatures, label = "Temperature (°C)") 
plt.plot(times, wind, label = "Wind speed (km/h)")
plt.plot(times, precipitation, label = "Precipitation")
plt.title('7 day weather forecast, hourly plot')
plt.xticks(rotation=90)

plt.xticks(np.arange(0, len(times)+1, 5))

plt.tight_layout() 
plt.legend()
plt.show()

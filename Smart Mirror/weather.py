#Author: Dustin Grady
#Function: Access weather data from Open Weather Maps
#Status: Working/Tested

import pyowm
import time

try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

API_KEY = 'f758480110064748fcea0d1f2063bbb3'
time1 = time.localtime(time.time())

class WeatherClass():
    def __init__(self):
        owm = pyowm.OWM(API_KEY)
        self.location = 'Santa Cruz, CA, USA'
        observation = owm.weather_at_place(self.location)
        weather = observation.get_weather()

        '''Get Current Weather Conditions'''
        self.currentWeather = str(weather.get_detailed_status())

        '''Get Current Temperature in Fahrenheit'''
        self.currentTemperature = weather.get_temperature(unit = 'fahrenheit')
        self.currentTemperature = str(self.currentTemperature).split("'temp':", 1)[1]#Get temperature, removing everything before it
        self.currentTemperature = str(self.currentTemperature[:3])#Remove everything except for the 2 digits we need

        '''Determine Weather Icon'''
        if "clouds" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Cloudy.png")
        if "clear" in self.currentWeather:
            if(time1.tm_hour > 6) and (time1.tm_hour <18):#Between 6am and 6pm will be day
                self.weatherImage = PhotoImage(file="ClearSkyDay.png")
            else:
                self.weatherImage = PhotoImage(file="ClearSkyNight.png")
        if "sunny" in self.currentWeather:
            self.weatherImage = PhotoImage(file="ClearSkyDay.png")
        if "rain" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Rain.png")
        if "thunder" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Thunder.png")
        if "snow" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Snow.png")
        if "haze" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")
        if "fog" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")
        if "mist" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")

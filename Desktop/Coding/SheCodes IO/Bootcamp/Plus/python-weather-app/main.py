import requests
from rich import print
from datetime import datetime
from config import api_key


def display_current_weather(city):
    """ Displays the current weather """
    
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
    
    response = requests.get(api_url)
    current_weather_data = response.json()
    current_weather_city = current_weather_data['city']
    current_weather_temperature = round(current_weather_data['temperature']['current'])
    
    print(f"The temperature in {current_weather_city} is {current_weather_temperature}°C")

def display_forecast_weather(city_name):
    """ Display the weather forecast of a city """
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"
   
    response = requests.get(api_url)
    forecast_weather_data = response.json()
    print("\n[bold yellow]Forecast:[/bold yellow]")

    
    for day in forecast_weather_data['daily']: # Loop through the daily list "[]" 
        timestamp = day['time']
        date = datetime.fromtimestamp(timestamp) # convert timestamp to date time
        formatted_day = date.strftime("%A") # %A is the code that represents how we want the date format style
        temperature = day['temperature']['day']

        if date.date() != datetime.today().date():
          print(f"{formatted_day}: {round(temperature)}°C")

def credit():
    """ Displays credit message """
    print("\n[italic]This app was built by Isabela Alcantara[/italic]")

def welcome():
    """ Displays welcome message """
    print("[purple bold]Welcome to my Weather App[/purple bold]")

welcome()
city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
    display_current_weather(city_name)
    
    display_forecast_weather(city_name)
    credit()
else: 
    print("Please try again with a city")
    
    
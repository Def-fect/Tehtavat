import requests

api_key = "b3f0dc46a021d01e466bdfc8d03c8726"
kaupunki= input ("anna kaupunki")


def get_weather():

    url = "http://api.openweathermap.org/data/2.5/weather"

    # params
    params = {
        'q': kaupunki,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params)

        weather_data = response.json()

        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        print(f"\nWeather in {kaupunki}:")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Temperature: {temperature}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Error parsing weather data. Please check the API response.")


get_weather()

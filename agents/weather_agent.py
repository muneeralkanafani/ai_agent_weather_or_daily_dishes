import re
import time
import requests

class WeatherAgent:

    def __init__(self, api_key):
        self.api_key = api_key
        self.geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        self.weather_url = "https://api.openweathermap.org/data/2.5/weather"
        self.memory = Memory()

    def answer(self, query):
        """return the answer about the weather from user's query"""
        city = self.extract_city(query)
        if not city:
            return "Please specify a city for weather information."
        lat, lon = self.get_geo(city)
        if lat is None or lon is None:
            return "Can't Get the coordinates from the city name"
        return self.get_weather(city, lat, lon)

    def get_geo(self, city):
        """get the coordinates from the city name using the openweather api"""
        params = {"q": city, "limit": 1, "appid": self.api_key}
        res = requests.get(self.geo_url, params=params, timeout=10)
        if res.status_code == 200 and res.json():
            loc = res.json()[0]
            return loc["lat"], loc["lon"]
        return None, None

    def get_weather(self, city, lat, lon):
        """get the weather from the coordinates using the openweather api"""
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.weather_url, params=params)
            response.raise_for_status()
            data = response.json()
            return self.format_weather_response(city, data)
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather data: {str(e)}"

    def extract_city(self, query):
        """extract the city name from the user's query"""
        query_lower = query.lower()
        patterns = [
            r'rain in (\w+)',
            r'weather in (\w+)',
            r'temperature in (\w+)',
            r'forecast for (\w+)',
            r'how is (\w+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, query_lower)
            if match:
                return match.group(1).capitalize()
        return None

    def format_weather_response(self, city, data):
        """format the response before return it"""
        previous = self.memory.recall(city)
        current_temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        self.memory.store(city, {
            "temp": current_temp,
            "description": description,
            "timestamp": time.time()
        })
        response = (
            f"The current weather in {city} is {description} "
            f"with a temperature of {current_temp}°C."
        )
        if previous:
            temp_change = current_temp - previous["temp"]
            response += f" (Temperature change: {temp_change:+.1f}°C)"
        return response

class Memory:

    def __init__(self):
        self.storage = {}
    
    def store(self, key, value):
        self.storage[key] = value
    
    def recall(self, key):
        return self.storage.get(key, None)
    
    def clear(self, key=None):
        if key:
            self.storage.pop(key, None)
        else:
            self.storage.clear()

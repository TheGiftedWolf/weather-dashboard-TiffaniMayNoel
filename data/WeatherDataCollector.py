import requests
from dataclasses import dataclass
# requests → lets you send HTTP requests (GET, POST, etc.) to the weather API.

# dataclass → a decorator that makes it easy to define classes that just hold data. It automatically adds __init__, __repr__, and __eq__ methods.
@dataclass
class WeatherData:
    city: str
    temperature: float
    condition: str

# Defines a simple structure for weather data.

# Has 3 fields:

# city → the city name as a string.

# temperature → the temperature as a float.

# condition → the weather condition (like “Clear”, “Rain”) as a string.

# Using @dataclass means you don’t need to write your own constructor — Python generates it for you.

# Why use this?

# Keeps your weather data organized.

# Makes it easy to pass around weather info as a single object.

# Improves code readability.
class WeatherDataCollector:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

# Defines a reusable class that knows how to talk to the weather API.

# __init__ method:

# Takes your api_key (so you can authenticate with OpenWeatherMap).

# Stores it as self.api_key for use in requests.

# Sets self.base_url to the OpenWeatherMap endpoint for current weather data.

# Why use this?
# Keeps your API logic separate from your GUI.

# Makes your code modular — you can reuse this collector anywhere you need weather data.

# Makes unit testing easier: you can test just the API logic without starting your full app.


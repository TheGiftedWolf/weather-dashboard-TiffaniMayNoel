import os
from dotenv import load_dotenv
from dataclasses import dataclass
# ##Imports os → lets you interact with your operating system’s environment variables.

# dotenv → load_dotenv() loads variables from a .env file into your environment so os.getenv() can access them.

# dataclass → simplifies defining a class that just holds data — it auto-generates the __init__, __repr__, and comparison methods.


# # Load environment variables from .env file
# This tells Python to find a .env file in your project folder (if you have one) 
# and load its contents into your system’s environment variables.

load_dotenv()

# The @dataclass decorator makes this class automatically handle storing its fields.

# This Config class is your one place to keep all settings your app needs.
@dataclass
class Config:
    """
    Application configuration.
    Holds all settings needed by the app.
    """
    API_KEY: str           # Required API key ;Must be set for your app to connect to the weather API.
    BASE_URL: str          # Base URL for weather API. the root URL for making API calls.
    database_path: str     # Path to SQLite database for storing weather data. Where you’ll store data locally.
    log_level: str = "INFO" # optional fields with default values; useful for controlling logging and request behavior.
    max_retries: int = 3   # optional fields with default values; useful for controlling logging and request behavior.
    request_timeout: int = 10  # optional fields with default values; useful for controlling logging and request behavior.

# This lets you call Config.from_environment() 
# to create a new Config object loaded directly from your system environment (or .env).

    @classmethod
    def from_environment(cls):
        """Load configuration from environment variables."""
        api_key = os.getenv('API_KEY')    #It tries to get the API_KEY from the environment.
        if not api_key:       #If it doesn’t exist, it raises an error so your app fails fast — you must have an API key to run.
            raise ValueError("API_KEY environment variable required")

        base_url = os.getenv('BASE_URL', 'http://api.openweathermap.org/data/2.5/weather') #If BASE_URL is not set, it uses the default OpenWeatherMap API URL.

        return cls(
            API_KEY=api_key,                # Matches dataclass field
            BASE_URL=base_url,              # Add BASE_URL here
            database_path=os.getenv('DATABASE_PATH', 'weather_data.db'), #These use reasonable default values so your app works even if they’re missing.
            log_level=os.getenv('LOG_LEVEL', 'INFO'),
            max_retries=int(os.getenv('MAX_RETRIES', '3')),
            request_timeout=int(os.getenv('REQUEST_TIMEOUT', '10'))
        )
# Your config.py securely loads settings from environment variables into a
#  neat Config object that your app can use everywhere, using best practices for secrets and defaults.
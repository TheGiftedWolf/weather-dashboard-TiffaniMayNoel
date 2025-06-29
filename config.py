import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv('API_KEY')
Base_URL = "http://api.openweathermap.org/data/2.5/weather"


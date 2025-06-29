import tkinter as tk
from tkinter import messagebox
import requests
import json
from datetime import datetime
import config  # Importing the configuration settings
from config import API_KEY, Base_URL  # Importing specific settings from config.py

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Dashboard")
        self.root.geometry("400x300")
        
        # API configuration
        self.api_key = config.API_KEY  # Using the API key from config.py
        self.base_url = config.Base_URL  # Using the base URL from config.py"
        
        self.setup_gui()
        
    def setup_gui(self):
        # Search frame
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=20)
        
        self.city_entry = tk.Entry(search_frame, width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        
        search_btn = tk.Button(search_frame, text="Get Weather", 
                              command=self.get_weather_click)
        search_btn.pack(side=tk.LEFT)
        
        # Display frame
        self.display_frame = tk.Frame(self.root, bg='lightgray')
        self.display_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Labels for weather info
        self.city_label = tk.Label(self.display_frame, text="", font=('Arial', 16))
        self.city_label.pack(pady=10)
        
        self.temp_label = tk.Label(self.display_frame, text="", font=('Arial', 24))
        self.temp_label.pack()
        
        self.desc_label = tk.Label(self.display_frame, text="", font=('Arial', 12))
        self.desc_label.pack(pady=5)
        
        self.update_label = tk.Label(self.display_frame, text="", font=('Arial', 10))
        self.update_label.pack()
    
    def get_weather_click(self):
        city = self.city_entry.get()
        if city:
            weather_data = self.fetch_weather(city)
            if weather_data:
                self.display_weather(weather_data)
                self.save_weather(weather_data)
    
    def fetch_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'imperial'
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                self.handle_errors(f"City '{city}' not found")
                return None
                
        except requests.exceptions.Timeout:
            self.handle_errors("Request timed out. Check your connection.")
            return None
        except Exception as e:
            self.handle_errors(f"An error occurred: {str(e)}")
            return None
    
    def display_weather(self, data):
        self.city_label.config(text=data['name'])
        self.temp_label.config(text=f"{round(data['main']['temp'])}°F")
        self.desc_label.config(text=data['weather'][0]['description'].title())
        self.update_label.config(text=f"Updated: {datetime.now().strftime('%I:%M %p')}")
    
    def save_weather(self, data):
        with open("data/weather_history.txt", "a") as f:
            f.write(f"{datetime.now()},{data['name']},{data['main']['temp']},{data['weather'][0]['description']}\n")
    
    def handle_errors(self, error_message):
        messagebox.showerror("Error", error_message)
    
    def run(self):
        self.root.mainloop()

# Run the app
if __name__ == "__main__":
    app = WeatherApp()
    app.run()


# def add_numbers(a, b):
#     """
#     Adds two numbers together.
    
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.
    
#     Returns:
#     int, float: The sum of the two numbers.
#     """
#     return a + b

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

import requests
def fetch_weather(city, state):
    try:
        url = f"{Base_URL}?q={city},{state},US&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "city not found"}

        data = response.json()
        temp_k = data.get("current", {}).get("temp_k")
        if temp_k is None:
            return {"error": "No weather data"}

        description = data.get("current", {}).get("condition", {}).get("text", "No description")
        temp_c = round(temp_k - 273.15, 1)

        return {
            "city": city,
            "temp_c": temp_c,
            "description": description
        }

    except requests.exceptions.RequestException:
        return {"error": "Network error"}
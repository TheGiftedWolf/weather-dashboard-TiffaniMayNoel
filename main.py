import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
from config import Config
from weather_tracker import WeatherTracker

class WeatherApp:
    def __init__(self, config: Config):
        self.root = tk.Tk()
        self.root.title("Weather Dashboard")
        self.root.geometry("400x300")

        self.tracker = WeatherTracker(self)

        self.API_KEY = config.API_KEY
        self.base_url = config.BASE_URL

        self.setup_gui()
     #  self.root → creates the main app window.

     # Sets title and size.

     # Loads API_KEY and base_url from the passed Config object.

     # Calls setup_gui() to build the user interface.

    def setup_gui(self):
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=20)

        self.city_entry = tk.Entry(search_frame, width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)

        search_btn = tk.Button(search_frame, text="Get Weather", command=self.get_weather_click)
        search_btn.pack(side=tk.LEFT)

        show_btn = tk.Button(self.root, text="Show Tracked Weather", command=self.tracker.show_tracked_weather)
        show_btn.pack(pady=5)

        self.display_frame = tk.Frame(self.root, bg='lightgray')
        self.display_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.city_label = tk.Label(self.display_frame, text="", font=('Arial', 16))
        self.city_label.pack(pady=10)

        self.temp_label = tk.Label(self.display_frame, text="", font=('Arial', 24))
        self.temp_label.pack()

        self.desc_label = tk.Label(self.display_frame, text="", font=('Arial', 12))
        self.desc_label.pack(pady=5)

        self.update_label = tk.Label(self.display_frame, text="", font=('Arial', 10))
        self.update_label.pack()
# Adds a search frame (for user input).

# Adds an entry box where the user types the city name.

# Adds a button that runs get_weather_click when clicked.

# Adds a display frame to show:

# The city name

# The temperature

# The weather description

# The last updated time

    def get_weather_click(self):
        city = self.city_entry.get()
        if city:
            weather_data = self.fetch_weather(city)
        if weather_data:
            self.display_weather(weather_data)
            self.save_weather(weather_data)
            self.tracker.add_city(city)  # NEW: add city to tracker

# Reads the city name from the input box.

# Calls fetch_weather(city) to get data from the API.

# If data comes back, it:

# Calls display_weather(data) to update the labels.

# Calls save_weather(data) to write the data to a file.

    def fetch_weather(self, city):
        try:
            url = f"{self.base_url}?q={city}&appid={self.API_KEY}&units=imperial"
            response = requests.get(url)
            if response.status_code != 200:
                self.handle_errors("City not found.")
                return None

            data = response.json()
            return {
                'name': data['name'],
                'main': {'temp': data['main']['temp']},
                'weather': [{'description': data['weather'][0]['description']}]
            }
        except Exception as e:
            self.handle_errors(str(e))
            return None
#  Builds the API URL with the city name and your API key.

# Sends an HTTP request to the weather API.

# Checks the response code:

# If it’s not 200 (success), shows an error message.

# If it’s successful:

# Parses the JSON.

# Returns a simplified dictionary with:

# name: city name

# main: current temp

# weather: weather description



    def display_weather(self, data):
        self.city_label.config(text=data['name'])
        self.temp_label.config(text=f"{round(data['main']['temp'])}°F")
        self.desc_label.config(text=data['weather'][0]['description'].title())
        self.update_label.config(text=f"Updated: {datetime.now().strftime('%I:%M %p')}")
# Updates all the GUI labels with the new weather data:
# City name
# Rounded temperature in °F
# Description with first letter capitalized
# Timestamp for when it was last updated

    def save_weather(self, data):
        with open("weather_history.txt", "a") as f:
            f.write(f"{datetime.now()},{data['name']},{data['main']['temp']},{data['weather'][0]['description']}\n")

# Appends the weather data to a file called weather_history.txt.
# Each line includes:
# Timestamp
# City
# Temperature
# Description

    def handle_errors(self, error_message):
        messagebox.showerror("Error", error_message)
# Uses messagebox.showerror to show a pop-up with the error message.

    def run(self):
        self.root.mainloop()
# Runs the Tkinter event loop so the window stays open and responds to user input.

if __name__ == "__main__":
    config = Config.from_environment()
    app = WeatherApp(config)
    app.run()

# Runs only when the script is executed directly.
# Calls Config.from_environment() to load your API key and base URL.
# Creates a new WeatherApp with the loaded config.
# Runs the app window.
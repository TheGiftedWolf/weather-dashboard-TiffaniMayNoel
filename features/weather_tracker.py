
import tkinter as tk
from tkinter import ttk, messagebox
from core.api import fetch_weather  # ✅ Import the standalone function

class WeatherTracker:
    def __init__(self, app):
        """
        Initializes the WeatherTracker with access to the main WeatherApp.
        """
        self.app = app
        self.tracked_cities = []  # List of city names the user has searched

    def add_city(self, city):
        """
        Add a city to the tracker if it's not already being tracked.
        """
        if city and city not in self.tracked_cities:
            self.tracked_cities.append(city)

    def get_tracked_cities(self):
        """
        Return the list of tracked cities.
        """
        return self.tracked_cities

    def show_tracked_weather(self):
        """
        Open a new window showing current weather for all tracked cities.
        """
        if not self.tracked_cities:
            self.app.handle_errors("No cities are being tracked yet.")
            return

        tracker_window = tk.Toplevel(self.app.root)
        tracker_window.title("Tracked Cities Weather")

        for city in self.tracked_cities:
            # ✅ Use the standalone fetch_weather function from core/api.py
            weather_data = fetch_weather(city, self.app.API_KEY, self.app.base_url)
            if weather_data:
                label = ttk.Label(
                    tracker_window,
                    text=f"{weather_data['name']}: {round(weather_data['main']['temp'])}°F, {weather_data['weather'][0]['description'].title()}"
                )
                label.pack(pady=2)
def save_tracker(self):
    try:
        with open("search_history.txt", "w") as file:
            for city in self.search_history:
                file.write(city + "\n")
            messagebox.showinfo("Saved", "Search history saved to search_history.txt.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save tracker: {e}")

def clear_history(self):
    self.search_history = []
    messagebox.showinfo("Cleared", "Search history has been cleared.")

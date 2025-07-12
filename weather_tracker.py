import tkinter as tk

class WeatherTracker:
    def __init__(self, app):
        """
        The tracker needs the main WeatherApp instance so it can use
        fetch_weather() and the Tkinter root for creating windows.
        """
        self.app = app
        self.tracked_cities = []  # Keeps a list of unique cities

    def add_city(self, city):
        """Add a city to the tracked list if it's not already tracked."""
        if city and city not in self.tracked_cities:
            self.tracked_cities.append(city)

    def get_tracked_cities(self):
        """Return all tracked cities."""
        return self.tracked_cities

    def show_tracked_weather(self):
        """Open a popup window showing latest weather for all tracked cities."""
        if not self.tracked_cities:
            self.app.handle_errors("No cities are being tracked yet.")
            return

        tracker_window = tk.Toplevel(self.app.root)
        tracker_window.title("Tracked Cities Weather")

        for city in self.tracked_cities:
            weather_data = self.app.fetch_weather(city)
            if weather_data:
                label = tk.Label(
                    tracker_window,
                    text=f"{weather_data['name']}: {round(weather_data['main']['temp'])}°F, {weather_data['weather'][0]['description'].title()}"
                )
                label.pack(pady=2)

# weather_tracker.py

import tkinter as tk
import threading
import pandas as pd
from pytube import YouTube
import vlc

class WeatherTracker:
    def __init__(self, app):
        """
        The tracker needs the main WeatherApp instance so it can use
        fetch_weather() and the Tkinter root for creating windows.
        """
        self.app = app
        self.tracked_cities = []  # Keeps a list of unique cities
        self.video_links = self.load_video_links()
        self.default_url = "https://youtu.be/SC4xMk98Pdc?si=GMq39cSv_z8vrU3t&t=19"

    def load_video_links(self, csv_path="video_links.csv"):
        df = pd.read_csv(csv_path)
        return dict(zip(df["weather_condition"], df["url"]))

    def play_audio_from_youtube(self, url):
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            audio_file = stream.download(filename="yt_audio.mp4")

            player = vlc.MediaPlayer(audio_file)
            player.play()

        except Exception as e:
            print("Error playing audio:", e)

    def start_audio_playback(self, condition):
        url = self.video_links.get(condition, self.default_url)
        threading.Thread(target=lambda: self.play_audio_from_youtube(url)).start()

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

                # Start audio based on weather condition
                condition = weather_data['weather'][0]['description'].title()
                self.start_audio_playback(condition)

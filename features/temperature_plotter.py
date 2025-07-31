# # features/temperature_plotter.py

import matplotlib.pyplot as plt
from datetime import datetime

def plot_temperature_history(file_path="weather_history.txt"):
    dates = []
    temps = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                try:
                    date = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                    temp = float(parts[2])
                    dates.append(date)
                    temps.append(temp)
                except ValueError:
                    continue  # skip any malformed lines

    if not dates:
        print("No valid data to plot.")
        return

#     plt.figure(figsize=(10, 5))
#     plt.plot(dates, temps, marker='o', linestyle='-', color='royalblue')
#     plt.title("Temperature Over Time")
#     plt.xlabel("Date")
#     plt.ylabel("Temperature (°F)")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.grid(True)
#     plt.show()
# # def save_temperature_plot(file_path="temperature_plot.png"):
# #     """


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def show_temperature_graph(city_name, file_path="weather_history.txt"):
    try:
        # Read the file into a DataFrame
        df = pd.read_csv(file_path, names=["timestamp", "city", "temperature", "description"], parse_dates=["timestamp"])

        # Clean the data
        df = df.dropna(subset=["timestamp", "city", "temperature"])
        df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
        df = df.dropna(subset=["temperature"])

        # Filter for selected city
        city_df = df[df["city"].str.lower() == city_name.lower()]
        if city_df.empty:
            print("No valid data to plot.")
            return

        # Plot
        plt.figure(figsize=(10, 5))
        plt.plot(city_df["timestamp"], city_df["temperature"], marker="o", linestyle="-")
        plt.title(f"Temperature Over Time in {city_name}")
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°F)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error generating graph: {e}")

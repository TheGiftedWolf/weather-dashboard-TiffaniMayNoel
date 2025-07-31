# features/city_comparison.py
import tkinter as tk
from tkinter import messagebox
from core.api import fetch_weather


def compare_cities_weather(app):
    def fetch_and_display():
        city1 = app.city1_entry.get()
        city2 = app.city2_entry.get()

        if not city1 or not city2:
            messagebox.showwarning("Input Error", "Please enter both city names.")
            return

        data1 = fetch_weather(city1, app.API_KEY, app.base_url)
        data2 = fetch_weather(city2, app.API_KEY, app.base_url)

        if data1 and data2:
            result_text = (
                f"{data1['name']}\nTemp: {round(data1['main']['temp'])} °F\nDesc: {data1['weather'][0]['description'].title()}\n\n"
                f"{data2['name']}\nTemp: {round(data2['main']['temp'])} °F\nDesc: {data2['weather'][0]['description'].title()}"
            )
            result_label.config(text=result_text)
        else:
            result_label.config(text="Failed to fetch data for one or both cities.")

    # Create popup window
    compare_window = tk.Toplevel(app.root)
    compare_window.title("Compare Two Cities")
    compare_window.geometry("400x300")

    tk.Label(compare_window, text="City 1:").pack(pady=5)
    app.city1_entry = tk.Entry(compare_window, width=30)
    app.city1_entry.pack(pady=5)

    tk.Label(compare_window, text="City 2:").pack(pady=5)
    app.city2_entry = tk.Entry(compare_window, width=30)
    app.city2_entry.pack(pady=5)

    tk.Button(compare_window, text="Compare", command=fetch_and_display).pack(pady=10)

    result_label = tk.Label(compare_window, text="", font=("Lucida", 12), wraplength=350, justify="left")
    result_label.pack(pady=10)

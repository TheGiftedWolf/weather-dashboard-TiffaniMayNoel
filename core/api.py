import requests
from tkinter import messagebox

def fetch_weather(city, api_key, base_url):
    try:
        url = f"{base_url}?q={city}&appid={api_key}&units=imperial"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("City not found.")

        data = response.json()
        return {
            'name': data['name'],
            'main': {'temp': data['main']['temp']},
            'weather': [{'description': data['weather'][0]['description']}]
        }
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None
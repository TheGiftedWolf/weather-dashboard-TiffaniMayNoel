from tkinter import PhotoImage

# def update_mascot(app, weather_description):
#     """Update the mascot image based on weather condition."""
#     if "rain" in weather_description.lower():
#         image_path = "assets/rainy.png"
#     elif "cloud" in weather_description.lower():
#         image_path = "assets/cloudy.png"
#     elif "snow" in weather_description.lower():
#         image_path = "assets/snowy.png"
#     elif "sun" in weather_description.lower() or "clear" in weather_description.lower():
#         image_path = "assets/sunny.png"
#     else:
#         image_path = "assets/default.png"

#     try:
#         mascot_image = PhotoImage(file=image_path)
#         app.mascot_label.config(image=mascot_image)
#         app.mascot_label.image = mascot_image  # Prevent garbage collection
#     except Exception as e:
#         print(f"Error loading mascot image: {e}")
def update_mascot(app, description):
    description = description.lower()

    if "rain" in description:
        mood = "☔ It's rainy — carry an umbrella!"
    elif "cloud" in description:
        mood = "🌥️ Cloudy skies — Daydream."
    elif "clear" in description or "sun" in description:
        mood = "😎 Sunny day! Wear shades!"
    elif "snow" in description:
        mood = "❄️ Brr! Bundle up for snow!"
    elif "storm" in description:
        mood = "🌩️ Storm incoming! Bracing yourself!"
    else:
        mood = "🤔 Weather unclear. Checking the radar..."

    app.mascot_label.config(text=mood)

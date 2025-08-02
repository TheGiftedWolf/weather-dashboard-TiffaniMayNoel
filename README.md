Tiffani May Noel

# 📜 License

This project is open source and free to use for educational purposes.

# 🌦️ Weather Dashboard Application

A desktop GUI app built with Python and Tkinter that allows users to check real-time weather data, track their city searches, and view visual temperature trends using the OpenWeather API.

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.10 or later
- pip package manager

### Installation

1. Clone or download this repository to your local machine.
2. Open a terminal in the project directory.
3. Install dependencies:

```bash
pip install requests matplotlib tk
```

4. Run the application:

```bash
python main.py
```

---

## 🚀 Usage Guide

- **Enter a City:** Type in any valid city name.
- **Choose Temperature Unit:** Select Fahrenheit or Celsius using the radio buttons.
- **View Weather:** Click the **Update** button to fetch and display:
  - Current temperature
  - Humidity
  - Precipitation level
  - Temperature trend chart
- **Save Tracker:** Use this button to log your search history.
- **Clear History:** Clears all saved cities from the tracker.
- **Exit:** Close the app using the window’s exit button.

---

## ✨ Feature Summary

- ✅ Real-time weather data from OpenWeather API
- ✅ Clean and responsive Tkinter GUI
- ✅ Line graph of temperature trends (Matplotlib)
- ✅ Tracker with Save and Clear options
- ✅ Inspirational quotes feature
- ✅ Input validation and error handling
- ✅ Modular folder structure using MVC pattern
- ✅ Support for future enhancements like YouTube music integration

---

## 📁 Project Structure

```
weather-dashboard/
├── assets/
├── core/
│   └── weather_api.py
├── controllers/
├── features/
│   ├── tracker.py
│   └── update_mascot.py
├── data/
│   └── preferences.json
├── main.py
└── README.md
```


# import tkinter as tk

# def setup_gui(self):
#         search_frame = tk.Frame(self.root)
#         search_frame.pack(pady=20)

#         self.city_entry = tk.Entry(search_frame, width=20)
#         self.city_entry.pack(side=tk.LEFT, padx=5)

#         search_btn = tk.Button(search_frame, text="Get Weather", command=self.get_weather_click)
#         search_btn.pack(side=tk.LEFT)

#         show_btn = tk.Button(self.root, text="Show Tracked Weather", command=self.tracker.show_tracked_weather)
#         show_btn.pack(pady=5)

#         self.display_frame = tk.Frame(self.root, bg='lightgray')
#         self.display_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

#         self.city_label = tk.Label(self.display_frame, text="", font=('Arial', 16))
#         self.city_label.pack(pady=10)

#         self.temp_label = tk.Label(self.display_frame, text="", font=('Arial', 24))
#         self.temp_label.pack()

#         self.desc_label = tk.Label(self.display_frame, text="", font=('Arial', 12))
#         self.desc_label.pack(pady=5)

#         self.update_label = tk.Label(self.display_frame, text="", font=('Arial', 10))
#         self.update_label.pack()
# # Adds a search frame (for user input).

# # Adds an entry box where the user types the city name.

# # Adds a button that runs get_weather_click when clicked.

# # Adds a display frame to show:

# # The city name

# # The temperature

# # The weather description

# # The last updated time


import tkinter as tk

def setup_gui(app):
    search_frame = tk.Frame(app.root)
    search_frame.pack(pady=20)

    app.city_entry = tk.Entry(search_frame, width=20)
    app.city_entry.pack(side=tk.LEFT, padx=5)

    search_btn = tk.Button(search_frame, text="Get Weather", command=app.get_weather_click)
    search_btn.pack(side=tk.LEFT)

    show_btn = tk.Button(app.root, text="Show Tracked Weather", command=app.tracker.show_tracked_weather)
    show_btn.pack(pady=5)

    app.display_frame = tk.Frame(app.root, bg='lightgray')
    app.display_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    app.city_label = tk.Label(app.display_frame, text="", font=('Arial', 16))
    app.city_label.pack(pady=10)

    app.temp_label = tk.Label(app.display_frame, text="", font=('Arial', 24))
    app.temp_label.pack()

    app.desc_label = tk.Label(app.display_frame, text="", font=('Arial', 12))
    app.desc_label.pack(pady=5)

    app.update_label = tk.Label(app.display_frame, text="", font=('Arial', 10))
    app.update_label.pack()

# import tkinter as tk

# def setup_gui(app):
#     app.city_entry = tk.Entry(app.root, width=40)
#     app.city_entry.pack(pady=10)
#     # app.city_entry = tk.Entry(search_frame, width=40, fg='grey')
#     app.city_entry.insert(0, "Enter city here")
#     app.city_entry.bind('<FocusIn>', lambda e: app._on_entry_click())
#     app.city_entry.bind('<FocusOut>', lambda e: app._on_focusout())
#     app.city_entry.pack(side=tk.LEFT, padx=5)

#     get_weather_btn = tk.Button(app.root, text="Get Weather", command=app.get_weather_click,  font=("Lucida", 20), width=20, height=3)
#     get_weather_btn.pack(pady=10)

#     show_tracked_btn = tk.Button(app.root, text="Show Tracked Weather", command=app.tracker.show_tracked_weather)
#     show_tracked_btn.pack()

#     app.display_frame = tk.Frame(app.root, bg="SystemButtonFace")
#     app.display_frame.pack(pady=50, padx=40, fill=tk.BOTH, expand=True)

#     app.city_label = tk.Label(app.display_frame, text="", font=('Lucida', 20, 'bold'))
#     app.city_label.pack(pady=10)

#     app.temp_label = tk.Label(app.display_frame, text="", font=('Lucida', 27))
#     app.temp_label.pack()

#     app.desc_label = tk.Label(app.display_frame, text="", font=('Lucida', 16))
#     app.desc_label.pack(pady=5)

#     app.update_label = tk.Label(app.display_frame, text="", font=('Lucida', 15))
#     app.update_label.pack()

#     app.quote_label = tk.Label(app.display_frame, text="", font=('Lucida', 15), wraplength=380, justify="center")
#     app.quote_label.pack(pady=10)

#     def _on_entry_click(app):
#         if app.city_entry.get() == "Enter city here":
#          app.city_entry.delete(0, "end")
#          app.city_entry.config(fg='lightgrey')

#     def _on_focusout(app):
#         if app.city_entry.get() == "":
#             app.city_entry.insert(0, "Enter city here")
#             app.city_entry.config(fg='lightgrey')


# import tkinter as tk

# def setup_gui(app):
#     # Placeholder logic
#     def on_entry_click(event):
#         if app.city_entry.get() == "Enter city here":
#             app.city_entry.delete(0, "end")
#             app.city_entry.config(fg='black')

#     def on_focusout(event):
#         if app.city_entry.get().strip() == "":
#             app.city_entry.insert(0, "Enter city here")
#             app.city_entry.config(fg='grey')

#     # Entry field setup
#     app.city_entry = tk.Entry(app.root, width=40, fg='grey', font=("Lucida", 14))
#     app.city_entry.insert(0, "Enter city here")
#     app.city_entry.bind('<FocusIn>', on_entry_click)
#     app.city_entry.bind('<FocusOut>', on_focusout)
#     app.city_entry.pack(pady=10)

#     # Get Weather button
#     get_weather_btn = tk.Button(app.root, text="Get Weather", command=app.get_weather_click,
#                                 font=("Lucida", 20), width=15, height=2)
#     get_weather_btn.pack(pady=10)

#     # Show Tracked Weather button
#     show_tracked_btn = tk.Button(app.root, text="Show Tracked Weather", command=app.tracker.show_tracked_weather,
#                                  font=("Lucida", 12))
#     show_tracked_btn.pack()

#     # Weather display frame
#     app.display_frame = tk.Frame(app.root, bg="SystemButtonFace")
#     app.display_frame.pack(pady=30, padx=40, fill=tk.BOTH, expand=True)

#     app.city_label = tk.Label(app.display_frame, text="", font=('Lucida', 20, 'bold'))
#     app.city_label.pack(pady=10)

#     app.temp_label = tk.Label(app.display_frame, text="", font=('Lucida', 27))
#     app.temp_label.pack()

#     app.desc_label = tk.Label(app.display_frame, text="", font=('Lucida', 16))
#     app.desc_label.pack(pady=5)

#     app.update_label = tk.Label(app.display_frame, text="", font=('Lucida', 15))
#     app.update_label.pack()

#     app.quote_label = tk.Label(app.display_frame, text="", font=('Lucida', 15),
#                                wraplength=380, justify="center")
#     app.quote_label.pack(pady=10)


import tkinter as tk
from features.temperature_plotter import show_temperature_graph
from features.temperature_plotter import plot_temperature_history
from features.city_comparison import compare_cities_weather


def setup_gui(app):
    graph_button = tk.Button(app.root, text="Show Temp Graph", command=lambda: show_temperature_graph(app.city_entry.get()))
    graph_button.pack(pady=5)

    # Placeholder logic
    def on_entry_click(event):
        if app.city_entry.get() == "Enter city here":
            app.city_entry.delete(0, "end")
            app.city_entry.config(fg='black')

    def on_focusout(event):
        if app.city_entry.get().strip() == "":
            app.city_entry.insert(0, "Enter city here")
            app.city_entry.config(fg='grey')

    # Clear function
    def clear_display():
        app.city_entry.delete(0, "end")
        app.city_entry.insert(0, "Enter city here")
        app.city_entry.config(fg='grey')
        app.city_label.config(text="")
        app.temp_label.config(text="")
        app.desc_label.config(text="")
        app.update_label.config(text="")
        app.quote_label.config(text="")

    # Entry field
    app.city_entry = tk.Entry(app.root, width=40, fg='grey', font=("Lucida", 14))
    app.city_entry.insert(0, "Enter city here")
    app.city_entry.bind('<FocusIn>', on_entry_click)
    app.city_entry.bind('<FocusOut>', on_focusout)
    app.city_entry.pack(pady=10)

    # Buttons
    get_weather_btn = tk.Button(app.root, text="Get Weather", command=app.get_weather_click,
                                font=("Lucida", 20), width=20, height=2)
    get_weather_btn.pack(pady=10)

    show_tracked_btn = tk.Button(app.root, text="Show Tracked Weather", command=app.tracker.show_tracked_weather,
                                 font=("Lucida", 12))
    show_tracked_btn.pack()

    compare_btn = tk.Button(app.root, text="Compare Cities", command=lambda: compare_cities_weather(app))
    compare_btn.pack(pady=5)

    clear_btn = tk.Button(app.root, text="Clear", command=clear_display,
                          font=("Lucida", 12), width=10)
    clear_btn.pack(pady=5)

    # Display area
    app.display_frame = tk.Frame(app.root, bg="SystemButtonFace")
    app.display_frame.pack(pady=30, padx=40, fill=tk.BOTH)

    app.city_label = tk.Label(app.display_frame, text="", font=('Lucida', 20, 'bold'))
    app.city_label.pack(pady=10)

    app.temp_label = tk.Label(app.display_frame, text="", font=('Lucida', 27))
    app.temp_label.pack()

    app.mascot_label = tk.Label(app.root, text="", font=("Lucida", 20, "bold"), fg="darkblue", bg="#add8e6")
    app.mascot_label.pack(pady=10)

    app.desc_label = tk.Label(app.display_frame, text="", font=('Lucida', 16))
    app.desc_label.pack(pady=5)

    app.update_label = tk.Label(app.display_frame, text="", font=('Lucida', 15))
    app.update_label.pack()

    app.quote_label = tk.Label(app.display_frame, text="", font=('Lucida', 15),
                               wraplength=380, justify="center")
    app.quote_label.pack(pady=10)

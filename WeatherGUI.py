import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from WeatherCheck import check_weather


class WeatherGUI:

    # Constructor to initialize the GUI
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x600")

        self.label = tk.Label(self.root, text="Enter City:")
        self.label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10, padx=10)

        self.button = tk.Button(self.root, text="Submit", command=self.submit)
        self.button.pack()

        self.temp_label = tk.Label(self.root, text="")
        self.temp_label.pack(pady=10, padx=10)

        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack(pady=10, padx=10)

        self.img_label = tk.Label(self.root)
        self.img_label.pack(pady=10, padx=10)

    # Get the user input in the widget and call the main functionality
    def submit(self):
        user_input = self.entry.get()
        # calls the main functionality in WeatherCheck
        temperature, weather_info, image_path = check_weather(user_input.title().strip())

        try:
            load = Image.open(image_path).resize((300, 300))
            render = ImageTk.PhotoImage(load)

            # displays the results in the widget
            self.temp_label['text'] = temperature
            self.info_label['text'] = weather_info
            self.img_label['image'] = render
            self.img_label.image = render

        except FileNotFoundError:
            messagebox.showerror("Error", "Image not found")

    def run(self):
        self.root.mainloop()


# runs the application
app = WeatherGUI()
app.run()



import tkinter as tk
from tkinter import ttk
import numpy as np

# Dataset en interpolatie
data_horsepower = [560, 720, 785, 900, 1100]  # Horsepower (hp)
data_time = [7.8, 6.3, 5.9, 5.3, 4.8]  # Time (s)
time_from_horsepower = np.poly1d(np.polyfit(data_horsepower, data_time, 3))  # Polynomiale fit

def horsepower_from_time(time):
    """Bereken horsepower vanuit tijd."""
    if not (4.8 <= time <= 8.0):
        return "Time out of bounds (4.8-8.0 s)."
    for hp in np.linspace(560, 1100, 1000):  # Scan met hoge precisie
        if abs(time_from_horsepower(hp) - time) < 0.05:
            return round(hp, 2)
    return "No solution found for the given time."

def calculate_result():
    """Voer berekeningen uit op basis van de geselecteerde optie."""
    try:
        input_value = float(entry.get())
        if option.get() == "Calculate Time from Horsepower":
            if 560 <= input_value <= 1100:
                result = time_from_horsepower(input_value)
                result_label.config(text=f"Time: {round(result, 2)} seconds")
            else:
                result_label.config(text="Error: Horsepower out of bounds (560-1100 hp).")
        elif option.get() == "Calculate Horsepower from Time":
            if 4.8 <= input_value <= 8.0:
                result = horsepower_from_time(input_value)
                result_label.config(text=f"Horsepower: {result} hp")
            else:
                result_label.config(text="Error: Time out of bounds (4.8-8.0 seconds).")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# GUI opzetten
root = tk.Tk()
root.title("BMW F10 M5 100-200 km/h Calculator")
root.geometry("400x300")
root.resizable(False, False)

# GUI-Elementen
title_label = ttk.Label(root, text="BMW F10 M5 100-200 km/h Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

subtitle_label = ttk.Label(root, text="Calculate Time (s) or Horsepower (hp)", font=("Arial", 12))
subtitle_label.pack(pady=5)

option = tk.StringVar(value="Calculate Time from Horsepower")
option_menu = ttk.Combobox(root, textvariable=option, state="readonly",
                           values=["Calculate Time from Horsepower", "Calculate Horsepower from Time"])
option_menu.pack(pady=10)

entry_label = ttk.Label(root, text="Enter your value:")
entry_label.pack()
entry = ttk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_result)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text="Result will be displayed here", font=("Arial", 12))
result_label.pack(pady=20)

# Start GUI
root.mainloop()


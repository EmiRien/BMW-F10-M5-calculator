import streamlit as st
import numpy as np

# Dataset and interpolation
data_horsepower = [560, 720, 785, 900, 1100]  # Horsepower (hp)
data_time = [7.8, 6.3, 5.9, 5.3, 4.8]  # Time (s)
time_from_horsepower = np.poly1d(np.polyfit(data_horsepower, data_time, 3))  # Polynomial fit

def horsepower_from_time(time):
    """Calculate horsepower based on time."""
    if not (4.8 <= time <= 8.0):
        return "Time out of bounds (4.8-8.0 s)."
    for hp in np.linspace(560, 1100, 1000):  # Scan with high precision
        if abs(time_from_horsepower(hp) - time) < 0.05:
            return round(hp, 2)
    return "No solution found for the given time."

# Streamlit app configuration
st.title("BMW F10 M5 100-200 km/h Calculator")
st.write("Calculate time (s) or horsepower (hp) for a BMW F10 M5.")

# User options
option = st.selectbox("Select a calculation:", 
                      ["Calculate Time from Horsepower", "Calculate Horsepower from Time"])

if option == "Calculate Time from Horsepower":
    horsepower = st.number_input("Enter horsepower (560-1100 hp):", min_value=560, max_value=1100, step=1)
    if st.button("Calculate Time"):
        result = time_from_horsepower(horsepower)
        st.success(f"Time: {round(result, 2)} seconds")

elif option == "Calculate Horsepower from Time":
    time = st.number_input("Enter time (4.8-8.0 seconds):", min_value=4.8, max_value=8.0, step=0.01)
    if st.button("Calculate Horsepower"):
        result = horsepower_from_time(time)
        st.success(f"Horsepower: {result} hp")

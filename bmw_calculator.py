import numpy as np

# Interpolatiepunten (op basis van verstrekte data)
data_horsepower = [560, 720, 785, 900, 1100]  # pk
data_time = [7.8, 6.3, 5.9, 5.3, 4.8]  # seconden
time_from_horsepower = np.poly1d(np.polyfit(data_horsepower, data_time, 3))  # Interpolatiefunctie

# Maximale tijd instellen
max_time = 8.0

# Functie om pk te berekenen vanuit tijd
def horsepower_from_time_adjusted(time, lower_bound=560, upper_bound=1100, step=0.1):
    if time < 4.8 or time > max_time:
        return f"Error: Time out of bounds (4.8-{max_time} s)."
    for hp in np.arange(lower_bound, upper_bound + step, step):
        if abs(time_from_horsepower(hp) - time) < 0.05:  # Acceptabele foutmarge
            return round(hp, 2)
    return "No solution found within bounds."

# Hoofdprogramma
def main():
    print("BMW F10 M5 100-200 km/u Calculator")
    print("1. Calculate Time from Horsepower")
    print("2. Calculate Horsepower from Time")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == "1":
        try:
            hp = float(input("Enter Horsepower (560-1100 pk): "))
            if 560 <= hp <= 1100:
                result = time_from_horsepower(hp)
                print(f"Time for {hp} pk: {round(result, 2)} seconds")
            else:
                print("Error: Horsepower out of bounds (560-1100 pk).")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "2":
        try:
            time = float(input("Enter Time (4.8-8.0 seconds): "))
            result = horsepower_from_time_adjusted(time)
            print(f"Horsepower for {time} seconds: {result} pk")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Please select 1 or 2.")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

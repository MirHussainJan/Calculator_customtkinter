import tkinter as tk
import math

root = tk.Tk()
root.title("Speedometer")
root.geometry("600x500")

digital_speed = tk.Label(root, font=("Arial", 20))
digital_speed.grid(row=0, column=0, columnspan=2, pady=5)  # Place digital_speed label in the first row spanning two columns

speedometer = tk.Canvas(root, width=400, height=400)
speedometer.grid(row=1, column=0, padx=20, pady=10)  # Place speedometer canvas in the second row, first column

# Function to draw the speedometer
def draw_speedometer():
    speedometer.create_arc(50, 50, 350, 350, start=0, extent=180, style=tk.ARC, width=2)

    for i in range(0, 101, 4):
        angle = 180 + (i * 1.8)  # Convert speed to angle (0 to 180 degrees)
        x = 200 + 160 * math.cos(math.radians(angle))
        y = 200 + 160 * math.sin(math.radians(angle))
        
        if i % 10 == 0:
            speedometer.create_text(x, y, text=str(i), font=("Arial", 12))
        else:
            x1 = 200 + 155 * math.cos(math.radians(angle))
            y1 = 200 + 155 * math.sin(math.radians(angle))
            speedometer.create_line(x1, y1, x, y, fill="red", width=0.5)
        
my_throttle = tk.Scale(root, from_=100, to=0, orient="vertical", length=300, command=lambda val: draw_needle(int(val)))
def draw_needle(value):
    angle = 180 + (value * 1.8)  # Convert value to angle (0 to 180 degrees)
    x = 200 + 120 * math.cos(math.radians(angle))  # Calculate x coordinate for the needle
    y = 200 + 120 * math.sin(math.radians(angle))  # Calculate y coordinate for the needle    
    speedometer.delete("needle")
    needle = speedometer.create_line(200, 180, x, y, fill="red", width=2, tag="needle")
    digital_speed.config(text=f'{value} km/h')
    return needle

draw_speedometer()
draw_needle(0)

my_throttle.grid(row=1, column=1, padx=20, pady=10, rowspan=2)  # Place my_throttle scale in the second row, second column, spanning two rows

root.mainloop()
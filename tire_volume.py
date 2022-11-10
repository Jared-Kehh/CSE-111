# This imports math signs and imports pi.
from cmath import pi
import math
from datetime import datetime
math.pi

# Asking for the width of the tire.
width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))

# Asking for the ratio of the tire.
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Asking for the diameter of the wheel.
diameter_of_tire = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Equation to find the volume of the tire.
volume =  (pi * width_of_tire**2) * aspect_ratio * ((width_of_tire * aspect_ratio) + (2540*diameter_of_tire)) / 10000000000

# Outputs the approximate volume in liters.
print(f"The approximate volume is {volume:.2f} liters")

# Shows the date for today.
date = datetime.now()

# This creates a file and puts the information of the tire and the date that it happened.
with open("volume.txt", "at") as volume_file:
    print(f"{date:%m-%d-%Y}", file = volume_file)
    print(width_of_tire, file = volume_file)
    print(aspect_ratio, file = volume_file)
    print(diameter_of_tire, file = volume_file)
    print(f"{volume:.2f}", file = volume_file)


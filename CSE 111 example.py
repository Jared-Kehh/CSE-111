import math
from math import sqrt
math.pi


def data():
    a = float(input("Enter number for a: "))
    b = float(input("Enter number for b: "))
    c = float(input("Enter number for c: "))
    d = float(input("Enter number for d: "))
    x = a / b * (a / (c**2 + d**2))
    return (f"{x:.3f}")

data = []
data.append([22, 66, 9])

def data_two(a, b, c):
    value_two = ((-b) + sqrt((b**2) - (4*a*c))) / (2*a)
    return value_two

for test in data:
    answer = data_two(test[0], test[1], test[2])
    print(answer)

def compute_area(r):
    return math.pi * r * r

radius = float(input("Please Enter a radius: "))

print(f"the area is: {compute_area(radius)}")
# Mason England
# CS1400 - 8:30

from math import pi, tan
import math


# function to store the equation to get the area of the polygon
def polygon_equation(n, s):
    return (n * math.pow(s, 2))/(4 * tan(pi/n))


lengths = []

num_of_sides = []

# get the length of each side, and number of sides, then calculate the area of each polygon
for i in range(4):
    lengths.append(int(input(F"How long should each side be for polygon number {i + 1}?: ")))
    num_of_sides.append(int(input(F"how many sides should polygon number {i + 1} have?: ")))
    n = num_of_sides[i]
    s = lengths[i]
    result = polygon_equation(n, s)
    print(F"Area of polygon number {i + 1} is: {result}")

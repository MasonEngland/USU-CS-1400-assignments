from drawly import *
from random import randint
import math

def setup():
    start("Pattern maker")
    set_speed(10)

def reset():
    set_color("white")
    rectangle(0,0, 1280, 720, stroke=0)
    draw()

def draw_rectangle_pattern(x, y, count, offset, width, height, rotation=0):
    base_angle = 360 / count

    for i in range(count):
        set_random_color()
        coords = get_distance_point(offset, base_angle * i) # hopefully this will spread the rectangles evenly
        rectangle(coords[0] + x, coords[1] + y, width, height, rotation_angle=(-base_angle * i) + rotation, stroke=1)
        draw()

def draw_circle_pattern(x, y, radius, offset, count):
    base_angle = 360 / count 

    for i in range(count):
        set_random_color()
        coords = get_distance_point(radius + offset, base_angle * i) # same as last pattern
        circle(coords[0] + x, coords[1] + y, radius, stroke=1)
        draw()

def draw_super_pattern(amount):
    for i in range(amount):
        rand_num = randint(0, 1)
        if rand_num == 1:
            draw_circle_pattern(randint(0, 1280), randint(0,720), randint(0,50), randint(50, 200), randint(0, 100))
        else:
            draw_rectangle_pattern(randint(0,1280), randint(0,720), randint(0,100), randint(50, 200), randint(20, 100), randint(20, 100), randint(0, 90))

def set_random_color():
    num = randint(0, 4)
    colors = ["blue", "green", "orange", "red", "purple"]
    set_color(colors[num])

def get_distance_point(distance, angle):
    x_pos = distance * math.cos(math.radians(angle))
    y_pos = distance * math.sin(math.radians(angle))
    return [x_pos, y_pos]

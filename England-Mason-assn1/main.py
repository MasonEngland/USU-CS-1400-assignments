# Mason England
# CS1400 - 8:30
import drawly
from drawly import *

# initialize the canvas
start("D'marcus had a bad day because his wife left", (800, 1000), "lightblue")

text(350, 100, "D'marcus", 32)

x_pos = 400
y_pos = 750
radius = 170

# draw the body
for i in range(3):
    set_color("black")
    circle(x_pos, y_pos, radius)
    set_color("white")
    circle(x_pos, y_pos, radius-3)
    radius -= 20
    y_pos -= 165
draw()

# draw the face
set_color("black")
circle(350, 400, 15)
circle(450, 400, 15)
draw()


arc(350, 450, 100, 40, 0, 180, 20)
draw()

start_pos = [400, 580]

# draw the buttons
for i in range(3):
    circle(start_pos[0], start_pos[1], 15)
    start_pos[1] += 50
draw()

poly_pos = [300, 280]


# draw his hat
def draw_hat(scalex: int, scaley: int):
    polygon_begin()
    add_poly_point(poly_pos[0], poly_pos[1])
    add_poly_point(poly_pos[0] + scalex, poly_pos[1])
    add_poly_point(poly_pos[0] + scalex, poly_pos[1] - scaley)
    add_poly_point(poly_pos[0] + scalex * 3, poly_pos[1] - scaley)
    add_poly_point(poly_pos[0] + scalex * 3, poly_pos[1])
    add_poly_point(poly_pos[0] + scalex * 4, poly_pos[1])
    add_poly_point(poly_pos[0] + scalex * 4, poly_pos[1] + scaley)
    add_poly_point(poly_pos[0], poly_pos[1] + scaley)
    add_poly_point(poly_pos[0], poly_pos[1])
    polygon_end()


draw_hat(50, 50)
draw()
set_color("darkgreen")
poly_pos = [310, 283]
draw_hat(45,45)
draw()

# draw arms
set_color("brown")
line(150, 750, 260, 580, 10)
line(540, 580, 650, 750, 10)
line(150, 750, 100, 750, 7)
line(150, 750, 115, 785, 7)
line(150, 750, 150, 790, 7)
line(650, 750, 680, 790, 7)
line(650, 750, 710, 750, 7)
line(650, 750, 650, 800, 7)
draw()

# add scenery
set_color("yellow")
circle(100, 100, 150)
draw()

set_color("green")
rectangle(0, 920, 900, 300)
draw()

done()

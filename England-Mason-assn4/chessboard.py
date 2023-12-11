from drawly import *



def draw_all_rectangles(start_x, start_y, width, height):
    interval_x = width / 20
    interval_y = height / 10

    devisor = 0
    print(interval_x)
    print(interval_y)
    for i in range(10):
        for j in range(20):
            if j % 2 == devisor:
                set_color("black")
                draw_rectangle((j * interval_x) + start_x, (i * interval_y) + start_y, interval_x, interval_y)
        if devisor == 1:
            devisor = 0
        else: 
            devisor = 1

def draw_rectangle(start_x, start_y, width, height, border = False):

    polygon_begin(0 if border != True else 1)
    for i in range(5):
        add_poly_point(start_x + width if i == 1 or i == 2 else start_x, start_y + height if i == 2 or i == 3 else start_y)
    polygon_end()
    draw()
    

def draw_chessboard(x, y, width = 250, height = 250):
    start()
    set_speed(10)
    draw_rectangle(x, y, width, height, True)
    draw_all_rectangles(x,y, width, height)
    done()
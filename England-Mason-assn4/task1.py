#### Add Import Statement(s) as needed ####
import drawly
from chessboard import * 
#### End Add Import Statement(s) ####

def main():
#### Add Code to get input from user ####
    print("Welcome to the chessboard genrator!")
    start_x = int(input("\tWhat should the starting x be?: "))
    start_y = int(input("\tWhat should the starting y be?: "))
    width = input("\tWhat should the width be?: ")
    height = input("\tWhat should the height be?: ")

#### End Add Code to get input from user ####

    if width == "" and height == "":
        draw_chessboard(start_x, start_y)
    elif height == "":
        draw_chessboard(start_x, start_y, width=int(width))
    elif width == "":
        draw_chessboard(start_x, start_y, height=int(height))
    else:
        draw_chessboard(start_x, start_y, int(width), int(height))

main()
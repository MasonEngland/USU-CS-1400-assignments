# Mason England
# cs 1400 - MWF 8:30 AM

from drawly import *

class Moody:
    def __init__(self, start_smile, start_happy, start_dark_eyes):
        self.smile = start_smile # this is a method
        self.happy = start_happy # this is a method 
        self.dark_eyes = start_dark_eyes # this is a method
    
    def draw_face(self):
        self.draw_head()
        self.draw_eyebrows()
        self.draw_eyes()
        self.draw_mouth()
        redraw()
    
    def change_mouth(self):
        self.smile = not self.smile
        self.draw_face()

    def change_emotion(self):
        self.happy = not self.happy
        self.draw_face()
        
    def change_eyes(self):
        self.dark_eyes = not self.dark_eyes
        self.draw_face()

    def is_smile(self):
        return self.smile
    def is_happy(self):
        return self.happy
    def is_dark_eyes(self):
        return self.dark_eyes
    
    def draw_eyes(self):
        set_color("black" if self.dark_eyes == True else "green")
        circle(1280/2 - 80, 720/2 - 20, 30)
        circle(1280/2 + 80, 720/2 - 20, 30 )
        set_color("black")

    def draw_head(self):
        set_color("black")
        circle(1280/2, 720/2, 200)
        set_color("white")
        circle(1280/2, 720/2, 190)
    
    # just for fun pls no take off points 
    def draw_eyebrows(self):
        set_color("black")
        rectangle(1280/2 - 100, 720/2 - 100, 100 , 20, 0, 0 if self.happy == True else -45)
        rectangle(1280/2, 720/2 - 100, 100 , 20, 0, 0 if self.happy == True else 45)

    def draw_mouth(self):
        if self.smile:
            arc(1280/2 - 50, 720/2 + 50, 100, 50, 180, 0)
        else:
            arc(1280/2 - 50, 720/2 + 50, 100, 50, 0, 180)

    

        





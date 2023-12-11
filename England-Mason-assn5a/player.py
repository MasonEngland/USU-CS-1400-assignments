# Mason England
# cs 1400 - MWF 8:30 AM

import pygame

class Player:
    def __init__(self, x:int, y: int, image: pygame.Surface):
        self.facing_left = True
        self.velocity = [0, 0]
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.radius = self.width / 2
        self.draw_position = [x, y]
        self.real_position = [x + self.radius, y + self.radius]
    
    def move_player(self):
        if (self.draw_position[0] + self.width >= 600 and self.velocity[0] > 0) or \
            (self.draw_position[0] <= 0 and self.velocity[0] < 0) or \
            (self.draw_position[1] <= 0 and self.velocity[1] < 0)  or \
            (self.draw_position[1] + self.height >= 600 and self.velocity[1] > 0):
            return 

        self.draw_position[0] += self.velocity[0]
        self.real_position[0] += self.velocity[0]
        self.draw_position[1] += self.velocity[1] 
        self.real_position[1] += self.velocity[1]

def make_player(x, y, image: pygame.Surface):
    return Player(x, y, image)
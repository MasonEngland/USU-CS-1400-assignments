# Mason England
# cs 1400 - MWF 8:30 AM

import pygame
from random import randint

class Coin:
    def __init__(self, image: pygame.Surface):
        self.image = image 
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw_position = [randint(0, 600 - self.width), randint(0 ,600 - self.height)]
        self.real_position = [self.draw_position[0] + (self.width /2), self.draw_position[1] + (self.height / 2)]
        self.radius = self.width
        

def make_coin(image):
    return Coin(image)


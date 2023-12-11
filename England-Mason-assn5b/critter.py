# Mason England
# CS 1400 - MWF 8:30 AM

import pygame
import math
from random import randint

def get_rand(num1, num2):
    list = [num1, num2]
    return list[randint(0, 1)]



class Critter:
    def __init__(self, screen: pygame.Surface , type, image: pygame.Surface):
        self.screen = screen 
        self.speed = 8
        self.type = type
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw_pos = [randint(0, 1280 - self.width), randint(0, 720 - self.height)]
        self.velocity = [get_rand(-1, 1), get_rand(-1, 1)]
        self.radius = self.width
        self.real_pos = [self.draw_pos[0] + (self.width / 2), self.draw_pos[1] + (self.height /2)]


    def move(self):
        self.check_bounce()

        self.draw_pos[0] += self.velocity[0] * self.speed
        self.real_pos[0] += self.velocity[0] * self.speed
        self.draw_pos[1] += self.velocity[1] * self.speed
        self.real_pos[1] += self.velocity[1] * self.speed



    def check_bounce(self):
        if self.draw_pos[0] < 0 or self.draw_pos[0] + self.width >= 1280:
            self.velocity[0] = -self.velocity[0]
        if self.draw_pos[1] < 0 or self.draw_pos[1] + self.height > 720:
            self.velocity[1] = -self.velocity[1]


    def did_get(self, mouse_pos: list | tuple):
        distance = math.sqrt((mouse_pos[0] - self.real_pos[0])**2 + (mouse_pos[1] - self.real_pos[1])**2)
        if distance < self.radius:
            return self.type
        return False
    
    def draw(self):
        self.screen.blit(self.image, self.draw_pos)
        





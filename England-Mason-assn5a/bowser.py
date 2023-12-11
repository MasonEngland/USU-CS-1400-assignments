# Mason England
# cs 1400 - MWF 8:30 AM

import pygame
from random import randint 
from time import time 

class Bowser:
    def __init__(self, x, y, image: pygame.Surface):
        self.sound = pygame.mixer.Sound("assets/Bump.wav")
        self.timer = time()
        self.speeds = [-1, 1]
        self.speed = 7
        self.draw_pos = [x, y]
        self.velocity = [1, 0]
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.real_position = [x + (self.width / 2), y + (self.height /2)]
        self.radius = self.width

    def move_bowser(self):

        # did this to make game more fun, pls don't take off points 
        if time() - self.timer >= 1:
            self.timer = time()
            self.velocity[0] = self.speeds[randint(0, 1)]
            self.velocity[1] = self.speeds[randint(0, 1)]


        #bowser bounces of the walls 
        if (self.draw_pos[0] + self.width >= 600 or self.draw_pos[0] < 00):
            self.sound.play()
            self.velocity[0] = -self.velocity[0]
        if (self.draw_pos[1] + self.height >= 600 or self.draw_pos[1] <= 0):
            self.sound.play()
            self.velocity[1] = -self.velocity[1]


        self.draw_pos[0] += self.velocity[0] * self.speed
        self.real_position[0] += self.velocity[0] * self.speed
        self.draw_pos[1] += self.velocity[1] * self.speed
        self.real_position[1] += self.velocity[1] * self.speed

def make_bowser(x, y, image):
    return Bowser(x, y, image)
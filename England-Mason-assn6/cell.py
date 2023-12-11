# Mason England 
# CS 1400 - MWF 8:30 AM  

import pygame
from player import Player

class Cell:
    def __init__(self, active, screen: pygame.Surface, pos: list, draw_facotor, color, image: pygame.Surface = None):
        self.__draw_pos = [pos[0] * draw_facotor, pos[1] * draw_facotor]
        self.__screen = screen 
        self.__image = image
        self.__rotated_image = pygame.transform.rotate(self.__image, 90) if image != None else None
        self.__active = active
        self.__width = self.__image.get_width() if image != None else None
        self.__height = self.__image.get_height() if image != None else None
        self.__color = color
    
    def draw(self):
        if self.__active:
            self.__screen.blit(self.__image, self.__draw_pos)

    # active cells the player drives over 
    def activate(self, player: Player, image: pygame.Surface, corner_image: pygame.Surface, color):
        player_pos = player.get_pos()

        if player_pos == self.__draw_pos:
            self.__color = color
            self.__active = True
            self.__set_image(image, corner_image, player)

    # check if player hit active cell 
    def did_hit(self, player: Player):
        player_pos = player.get_pos()
        if self.__active and player_pos == self.__draw_pos:
            return player.get_color()
        return None

    def get_pos(self):
        return self.__draw_pos
    
    # logic that determines which images the cell displays if the cell is active
    # main purpose is to handle corners 
    def __set_image(self, image: pygame.Surface, corner_image: pygame.Surface, player: Player):
        keys = pygame.key.get_pressed()
        #facing = player.get_facing()

        if self.__active and self.__color == "red":
            if player.get_facing() == 0 and (keys[pygame.K_LEFT]) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                self.__image = pygame.transform.flip(corner_image, True, False)
            elif player.get_facing() == 0 and (keys[pygame.K_RIGHT]) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                self.__image = corner_image
            elif player.get_facing() == 1 and (keys[pygame.K_LEFT]) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                self.__image = pygame.transform.flip(corner_image, True, True)
            elif player.get_facing() == 1 and (keys[pygame.K_RIGHT]) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                self.__image = pygame.transform.flip(corner_image, False, True)
            elif player.get_facing() == 2 and (keys[pygame.K_UP]) and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.__image = pygame.transform.flip(corner_image, False, True)
            elif player.get_facing() == 2 and (keys[pygame.K_DOWN]) and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.__image = corner_image
            elif player.get_facing() == 3 and (keys[pygame.K_UP]) and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.__image = pygame.transform.flip(corner_image, True, True)
            elif player.get_facing() == 3 and (keys[pygame.K_DOWN]) and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.__image = pygame.transform.flip(corner_image, True, False)
            else:
                self.__rotated_image = pygame.transform.rotate(image, 90)
                self.__image = image if player.get_facing() == 0 or player.get_facing() == 1 else self.__rotated_image

        
        elif self.__active and self.__color == "blue":
            if player.get_facing() == 0 and (keys[pygame.K_a]) and not (keys[pygame.K_w] or keys[pygame.K_s]):
                self.__image = pygame.transform.flip(corner_image, True, False)
            elif player.get_facing() == 0 and (keys[pygame.K_d]) and not (keys[pygame.K_w] or keys[pygame.K_s]):
                self.__image = corner_image
            elif player.get_facing() == 1 and (keys[pygame.K_a]) and not (keys[pygame.K_w] or keys[pygame.K_s]):
                self.__image = pygame.transform.flip(corner_image, True, True)
            elif player.get_facing() == 1 and (keys[pygame.K_d]) and not (keys[pygame.K_w] or keys[pygame.K_s]):
                self.__image = pygame.transform.flip(corner_image, False, True)
            elif player.get_facing() == 2 and (keys[pygame.K_w]) and not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.__image = pygame.transform.flip(corner_image, False, True)
            elif player.get_facing() == 2 and (keys[pygame.K_s]) and not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.__image = corner_image
            elif player.get_facing() == 3 and (keys[pygame.K_w]) and not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.__image = pygame.transform.flip(corner_image, True, True)
            elif player.get_facing() == 3 and (keys[pygame.K_s]) and not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.__image = pygame.transform.flip(corner_image, True, False)
            else:
                self.__rotated_image = pygame.transform.rotate(image, 90)
                self.__image = image if player.get_facing() == 0 or player.get_facing() == 1 else self.__rotated_image


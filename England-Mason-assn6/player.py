# Mason England 
# CS 1400 - MWF 8:30 AM  

import pygame 


class Player:
    def __init__(self, screen: pygame.Surface, x ,y, color, turn: pygame.mixer.Sound, image: pygame.Surface):
        self.__screen = screen 
        self.__turn = turn
        self.__facing = 0 
        self.__draw_factor = 10
        self.__velocity = [0,-1 * 10]
        self.__pos = [x, y]
        self.__current_image = image
        self.__image_up = image
        self.__image_left = pygame.transform.rotate(image, 90)
        self.__image_down = pygame.transform.flip(image, True, False)
        self.__image_right = pygame.transform.rotate(image, 260)
        self.__color = color

    def draw(self):
        self.move()
        self.__screen.blit(self.__current_image, [self.__pos[0] - 3, self.__pos[1] - 3])
    
    def get_facing(self):
        return self.__facing

    def get_color(self):
        return self.__color
    
    def move(self):
        self.__turn.set_volume(0.2)
        keys = pygame.key.get_pressed() # most keyboard inputs are handled here 
        if self.__color == "blue":
            if keys[pygame.K_w]:
                self.__turn.play()
                self.__facing = 0
                self.__current_image = self.__image_up
                self.__velocity[0] = 0
                self.__velocity[1] = -1 * self.__draw_factor
            elif keys[pygame.K_s]:
                self.__turn.play()
                self.__facing = 1
                self.__current_image = self.__image_down
                self.__velocity[0] = 0
                self.__velocity[1] = 1 * self.__draw_factor
            elif keys[pygame.K_a]:
                self.__turn.play()
                self.__facing = 2
                self.__current_image = self.__image_left
                self.__velocity[1] = 0
                self.__velocity[0] = -1 * self.__draw_factor
            elif keys[pygame.K_d]:
                self.__turn.play()
                self.__facing = 3
                self.__current_image = self.__image_right
                self.__velocity[1] = 0
                self.__velocity[0] = 1 * self.__draw_factor
            

        if self.__color == "red":
            if keys[pygame.K_UP]:
                self.__turn.play()
                self.__facing = 0
                self.__current_image = self.__image_up
                self.__velocity[0] = 0
                self.__velocity[1] = -1 * self.__draw_factor
            elif keys[pygame.K_DOWN]:
                self.__turn.play()
                self.__facing = 1
                self.__current_image = self.__image_down
                self.__velocity[0] = 0
                self.__velocity[1] = 1 * self.__draw_factor
            elif keys[pygame.K_LEFT]:
                self.__turn.play()
                self.__facing = 2
                self.__current_image = self.__image_left
                self.__velocity[1] = 0
                self.__velocity[0] = -1 * self.__draw_factor
            elif keys[pygame.K_RIGHT]:
                self.__turn.play()
                self.__facing = 3
                self.__current_image = self.__image_right
                self.__velocity[1] = 0
                self.__velocity[0] = 1 * self.__draw_factor
        self.__pos[0] += self.__velocity[0]
        self.__pos[1] += self.__velocity[1]
            

    def get_pos(self):
        return self.__pos
    
    def did_hit_wall(self, screen_dimensions: list):
        if self.__pos[0] <= 0 or self.__pos[0] + self.__current_image.get_width() >= screen_dimensions[0]:
            return True
        if self.__pos[1] <= 0 or self.__pos[1] + self.__current_image.get_height() >= screen_dimensions[1]:
            return True 
        
        return False

    # called during game reset 
    def reset_pos(self, coords):
        self.__current_image = self.__image_up
        self.__velocity = [0, -1 * 10]
        self.__facing = 0
        self.__pos = coords
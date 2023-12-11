# Mason England
# CS 1400 MWF - 8:30AM

import pygame
from cursor import Cursor
from critter import Critter
import time
import math

SCREEN_WIDTH = 1280  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "Bug Catcher"


def make_critter_list(count, screen: pygame.Surface, images: list):
    main_list = []
    for i in range(count // 2):
        main_list.append(Critter(screen, "good", images[0]))
    for i in range(count // 2):
        main_list.append(Critter(screen, "bad", images[1]))

    return main_list


def check_collision(critter_list, cursor, mouse_pos, catch_sound):
    temp_list = []
    for critter in critter_list:
        if not (critter.did_get(mouse_pos) == "good" and cursor == True) and not (critter.did_get(mouse_pos) == "bad" and cursor == False):
            temp_list.append(critter)
        else:
            catch_sound.play()
    return temp_list

def check_game_over(critter_list, cursor, mouse_pos):
    for critter in critter_list:
        if (critter.did_get(mouse_pos) == "good" and cursor == False) or (critter.did_get(mouse_pos) == "bad" and cursor == True):
            return True 
    return False



def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()


    # Set up game components
    # images, sounds, other data necessary for game play
    current_cursor = True
    cursor = Cursor("Bug_Net_sticker.png")
    background = pygame.image.load("Forest-background.png")
    woosh_sound = pygame.mixer.Sound("woosh.wav")
    spray_sound = pygame.mixer.Sound("spray.wav")
    catch_sound = pygame.mixer.Sound("catch.mp3")
    background_music = pygame.mixer.music.load("background_music.wav")
    # Set up game data
    font = pygame.font.SysFont("sfpro", 32)
    can_click = False
    pygame.mouse.set_visible(False)
    won = False
    critter_count = 10
    critter_list = make_critter_list(critter_count, screen, [pygame.image.load("dragonfly.png"), pygame.image.load("wasp.png")])
    init_time = time.time()
    change_time = True


    # Game Loop
    game_over = False
    running = True

    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the window's X button
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    ### Do Stuff to Reset Game ###
                    game_over = False

        screen.blit(background, [0, 0], pygame.Rect(0 ,0, 1280, 720))

        
        # Update state of components/data
        mouse_pos = pygame.mouse.get_pos()
        cursor.update_pos([mouse_pos[0] - cursor.image.get_width() / 2, mouse_pos[1] - cursor.image.get_height() / 2])
        # Always Update 

        # cause game over when critters are gone 
        if len(critter_list) == 0:
            game_over = True
            won = True

        if not game_over:
            mouse_pressed = pygame.mouse.get_pressed()
            if not mouse_pressed[2] and can_click == False:
                can_click = True

            # right click to switch modes
            if mouse_pressed[2] and can_click == True:
                current_cursor = not current_cursor
                cursor.image = pygame.image.load("Bug_Net_sticker.png") if current_cursor == True else pygame.image.load("spraycan.png")
                can_click = False

            
            for critter in critter_list:
                critter.move()
                critter.draw()

            if mouse_pressed[0]:
                if current_cursor == True:
                    woosh_sound.play()
                else:
                    spray_sound.play()

                critter_list = check_collision(critter_list, current_cursor, mouse_pos, catch_sound)
                game_over = check_game_over(critter_list, current_cursor, mouse_pos)

        if game_over:
            pygame.mixer.music.stop()
            screen.blit(font.render("You Won!! press enter for next round" if won else "Game OVER!! press enter to restart", True, "white"), [1280/ 2 - 200, 40])
            if (won) and change_time:
                current_time = round(time.time() - init_time, 4)
                change_time = False
            screen.blit(font.render(F"Time was {current_time}", True, "White"), [1280/2 - 200, 80])
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                critter_count = critter_count + 10 if won else 10
                critter_list = make_critter_list(critter_count, screen, [pygame.image.load("dragonfly.png"), pygame.image.load("wasp.png")])
                init_time = time.time()
                game_over = False 
                change_time = True
                won = False
                pygame.mixer.music.play(-1)


        # Update Display
        # Always Display 
        cursor.draw(screen)
        # Draw changes the screen 
        pygame.display.flip()
    
        # Define the refresh rate of the screen
        clock.tick(CLOCK_TICK)


main()


# Mason England 
# cs 1400 - MWF 8:30 AM


import pygame
from player import make_player 
from bowser import make_bowser
from random import randint
from coin import make_coin
import math

# -- Constants 
SCREEN_WIDTH = 600 # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600
CLOCK_TICK = 30
TITLE = "Mario MAMA MIA"


def main():
# Setup the pygame window and clock
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(7)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    ##########
    # Set up game media images, sounds

    pygame.mixer.music.load("./assets/desert-palace-trimmed.mp3") # wrote this piece myself
    die_sound = pygame.mixer.Sound("assets/Bowser Die.wav")
    coin_sound = pygame.mixer.Sound("assets/Coin.wav")
    win_sound = pygame.mixer.Sound("assets/1up.wav")
    background = pygame.image.load("assets/Mushroom_Kingdom.jpg")
    mario = pygame.image.load("assets/player.png")
    bowser = pygame.image.load("assets/bowser.png")
    coin = pygame.image.load("assets/coin.png")



    # -- Set up game data
    font = pygame.font.SysFont("sfpro", 32)
    won = False
    coin_count = 0
    player_speed = 5
    player = make_player(280, 480, mario)
    enemy = make_bowser(300, 300, bowser)

    def did_touch(player: player, item):
        distance = math.sqrt(abs(player.real_position[0] - item.real_position[0])**2 + (player.real_position[1] - item.real_position[1])**2)
        if distance <= player.radius or distance <= item.radius:
            return True 
        return False 
    
    coin_list = [
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
        make_coin(coin),
    ]

   
    #  -- Game Loop
    game_over = False
    running = True
    pygame.mixer.music.play(-1)
    while running:
        # Redraw the backgorund 
        screen.blit(background, [0, 0])

        # Get Input/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # User clicked the window's X button
                running = False
                
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and game_over:
            # Do Stuff to Reset Game
            game_over = False 
            won = False
            coin_list = [
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
                make_coin(coin),
            ]
            player = make_player(280, 480, mario)
            coin_count = 0
            enemy = make_bowser(300, 300, bowser)
            pygame.mixer.music.play(-1)
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            player.velocity[1] = -1 * player_speed 
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            player.velocity[1] = 1 * player_speed
        else:
            player.velocity[1] = 0
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            if player.facing_left == False:
                player.image = pygame.transform.flip(player.image, True, False)

            player.facing_left = True 
            player.velocity[0] = -1 * player_speed
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            if player.facing_left == True:
                player.image = pygame.transform.flip(player.image, True, False)
                
            player.facing_left = False
            player.velocity[0] = 1 * player_speed
        else:
            player.velocity[0] = 0
        #### Add additional lines for other keys as necessary
        # Update state of components/data

        #### Always Update ####
        pass
        #### Update if Game is Not Over ###
        if not game_over:

        ### In this block of code game_over = True will happen ###
            if did_touch(player, enemy):
                die_sound.play()
                game_over = True
                won = False
            if len(coin_list) <= 0:
                win_sound.play()
                game_over = True
                won = True
            temp_list = []
            for item in coin_list:
                screen.blit(item.image, [item.draw_position[0], item.draw_position[1]])
                if not did_touch(player, item):
                    temp_list.append(item)
                else:
                    coin_sound.play()
                    coin_count += 1
            coin_list = temp_list
            enemy.move_bowser()
            screen.blit(enemy.image, enemy.draw_pos)
            player.move_player()
            screen.blit(player.image, player.draw_position)

        # Update if Game is Over 
        elif game_over:
            pygame.mixer.music.stop()
            if won :
                screen.blit(font.render("YOU WON!", 1, "black", None),[230, 30])
            else:
                screen.blit(font.render("GAME OVER!", 1, "black", None),[200, 30])

                
        #### Draw changes the screen ####
        pygame.display.flip()
        #### Define the refresh rate of the screen ####
        clock.tick(CLOCK_TICK)
main()




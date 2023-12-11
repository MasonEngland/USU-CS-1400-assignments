# Mason England 
# CS 1400 - MWF 8:30 AM  
import pygame 
from cell import *
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WINDOW_TITLE = "Crashtropolis"
CLOCK_TICK = 30

def main():
    
    ## -- initialize initial setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    ## -- add assets 
    background = pygame.image.load("./assets/images/grid.png")
    blue_straight = pygame.image.load("./assets/images/blue-straight.png")
    red_straight = pygame.image.load("./assets/images/red-straight.png")
    blue_car = pygame.image.load("./assets/images/blue-car.png")
    red_car = pygame.image.load("./assets/images/red-car.png")
    blue_corner = pygame.image.load("./assets/images/blue-corner.png")
    red_corner = pygame.image.load("./assets/images/red-corner.png")
    font = pygame.font.SysFont("sfpro", 32)
    crash = pygame.mixer.Sound("./assets/sounds/crash.wav")
    turn1 = pygame.mixer.Sound("./assets/sounds/turn-1.mp3")
    turn2 = pygame.mixer.Sound("./assets/sounds/turn-2.mp3")
   
    cell_size = 10 
    row_count = SCREEN_HEIGHT // cell_size 
    col_count = SCREEN_HEIGHT // cell_size
    grid = []

    blue_player = Player(screen, 150 , 750 , "blue", turn1, blue_car)
    red_player = Player(screen, 600, 750, "red", turn2, red_car )
    players = [blue_player, red_player]

    # Make the game grid 
    for col in range(col_count):
        grid.append([])
        for row in range(row_count):
            grid[col].append(Cell(False, screen, [col, row],cell_size, "", blue_straight))

    running = True
    game_over = False 
    player_lost = ""

    pygame.mixer.music.load("./assets/sounds/background-music.mp3")
    pygame.mixer.music.play(-1)

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE and game_over:
                    print("Space pressed")
                    
        screen.blit(background, (0,0))

        if not game_over:

            # do things for each cell in the grid 
            for i in range(len(grid)):
                for j in grid[i]:
                    for player in players:
                        if j.did_hit(player) != None:
                            crash.play()
                            pygame.mixer.music.load("./assets/sounds/gameover-music.mp3")
                            pygame.mixer.music.play(-1)
                            player_lost = j.did_hit(player)
                            game_over = True
                    j.activate(blue_player, blue_straight, blue_corner, "blue")
                    j.activate(red_player, red_straight, red_corner, "red")
                    j.draw() 
                    
            # do things for each player in the game
            for player in players:
                if player.did_hit_wall([SCREEN_WIDTH, SCREEN_HEIGHT]):
                    crash.play()
                    pygame.mixer.music.load("./assets/sounds/gameover-music.mp3")
                    pygame.mixer.music.play(-1)
                    player_lost = player.get_color()
                    game_over = True

            blue_player.draw()
            red_player.draw()

        if game_over:

            # diplay gameover screen 
            screen.blit(font.render("GAME OVER!!", True, "white"), [300, 60])
            screen.blit(font.render("Blue Wins!" if player_lost == "red" else "Red Wins!", True, "white"), [320, 100])
            screen.blit(font.render("Press SPACE to play again", True, "white"), [230, 400])

            # reset game when space bar is pressed 
            keys= pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                pygame.mixer.music.load("./assets/sounds/background-music.mp3")
                pygame.mixer.music.play(-1)
                grid = []
                for col in range(col_count):
                    grid.append([])
                    for row in range(row_count):
                        grid[col].append(Cell(False, screen, [col, row],cell_size, "", blue_straight)) 
                blue_player.reset_pos([150, 750])
                red_player.reset_pos([600, 750])
                game_over = False


        # Update display 
        pygame.display.flip()
        clock.tick(CLOCK_TICK)
main()

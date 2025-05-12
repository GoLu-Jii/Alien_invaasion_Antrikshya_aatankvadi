import pygame
import sys
import random

from game import Game


pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 650
OFFSET = 50

WHITE = (255, 255, 255)
BLACK = (0,0,0)

font = pygame.font.Font("font/font1.ttf", 30)
level_surface = font.render("LEVEL 01  ", False, BLACK)
game_over_surface = font.render("GAME OVER", False, BLACK)
score_text_surfce = font.render("SCORE", False, BLACK)
highscore_text_surfce = font.render("HIGH-SCORE", False, BLACK)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Antrix Aatankvadi")

clock = pygame.time.Clock()  #fps


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)


MYSTERYSHIP = pygame. USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))


#setp the game loop
while True:
    for event in pygame.event.get():        # game ke andar ke sare events ko control
        if event.type == pygame.QUIT:      # if game quit 
            pygame.quit()                      
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset() 
            
    
    #updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        #game.alien_shoot_laser()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collision()

    
    #drawing
    SCREEN.fill(WHITE)  
    pygame.draw.rect(SCREEN, BLACK , (10,10,780,730) , 2,0,60,60,60,60)
    pygame.draw.line(SCREEN, BLACK , (15,670) , (780,670),3)
    
    if game.run:
        SCREEN.blit(level_surface, (590, 690, 40 ,40 ))
    else:
        SCREEN.blit(game_over_surface, (540, 690, 40 ,40 ))
    
    life_image = pygame.transform.scale(game.spaceship_group.sprite.image, (50, 50))     
    x = 50
    for life in range(game.life):
        SCREEN.blit(life_image, (x, 682.5))
        x += 60
    SCREEN.blit(score_text_surfce, (50,15,50,50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, BLACK)
    SCREEN.blit(score_surface, (50,40,50,50))
    SCREEN.blit(highscore_text_surfce, (500,15,50,50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, BLACK)
    SCREEN.blit(highscore_surface, (550,40,50,50))
        
    game.spaceship_group.draw(SCREEN)
    game.spaceship_group.sprite.lasers_group.draw(SCREEN)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(SCREEN)
    game.aliens_group.draw(SCREEN)
    game.alien_lasers_group.draw(SCREEN)
    game.mystery_ship_group.draw(SCREEN)


         
    pygame.display.update()    #set game window 
    clock.tick(60)             #set fps

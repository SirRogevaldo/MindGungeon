import pygame, sys
from player import Gunman
from commands import InputHandler

#Constants
WIDTH, HEIGHT = 1920, 1080
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

inHandler = InputHandler()

#Player Initialization
player = Gunman(WIDTH/2, HEIGHT/2)

#Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    inHandler.handleInput(pygame.key.get_pressed(), player)
        
    #Draw
    display.fill((12, 24, 36))
    pygame.draw.rect(display, "brown", (WIDTH/10, HEIGHT/10, WIDTH*4/5, HEIGHT*4/5))  
    player.draw(display)

    #update
    player.update()
    pygame.display.flip()

    clock.tick(120)
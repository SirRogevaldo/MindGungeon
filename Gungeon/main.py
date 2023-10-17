import pygame, sys
from bullets import Bullet
from player import Gunman
from commands import InputHandler

#Constants
WIDTH, HEIGHT = 1600, 900
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

inHandler = InputHandler()

bullets = []

pygame.mouse.set_visible(False)

#Player Initialization
player = Gunman(WIDTH/2, HEIGHT/2)

#Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            #print(x,y)
            b = Bullet("orange", player.x, player.y, 20,20, 10, x,y)
            bullets.append(b)
            #ef __init__(self, color, x, y, width, height, speed, targetx,targety):
    
    inHandler.handleInput(pygame.key.get_pressed(), player)
        
    bullets_on_screen = []
    #Draw
    for b in bullets:
        b.move()

        if 0 <= b.x <= WIDTH and 0 <= b.y <= HEIGHT:
            bullets_on_screen.append(b)
    
    bullets = bullets_on_screen
    #print(len(bullets))

    display.fill((12, 24, 36))
    pygame.draw.rect(display, (60,60,60), (WIDTH/10, HEIGHT/10, WIDTH*4/5, HEIGHT*4/5))  
    for b in bullets:
        b.draw(display)

    # Mouse
    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(display, (255,0,0), (x, y), 15)
    pygame.draw.circle(display, (0,0,0), (x, y), 10)
    pygame.draw.circle(display, (255,0,0), (x, y), 5)

    player.draw(display)

    #update
    player.update()
    pygame.display.flip()

    clock.tick(120)
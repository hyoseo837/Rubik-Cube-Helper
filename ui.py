import pygame
import math
import random
import os
location = os.path.dirname(os.path.abspath(__file__))

pygame.init()

screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("cube solver")

clock = pygame.time.Clock()

aaFont = pygame.font.Font(None, 20)

coordinates = [(100,100),(100,250),(150,200)]
canvas = pygame.Surface((300,300))

running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
    
    text = aaFont.render(f"text", True,(255,255,255))


    # screen.blit(background, (0, 0))
    

    pygame.draw.polygon(canvas, (255,255,0), coordinates)
    screen.blit(canvas, (0,0))
    screen.blit(text,(30,30))

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
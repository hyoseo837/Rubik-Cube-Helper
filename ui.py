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
background = pygame.image.load("images/background.png")

coordinates = [(275,50),(405,125),(405,275),(275,350),(145,275),(145,125)]
shapes = [[(405,125),(405,275),(275,350),(275,200)],[(275,350),(145,275),(145,125),(275,200)],[(145,125),(275,50),(405,125),(275,200)]]
canvas = pygame.Surface((550,400))

running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
    
    text = aaFont.render(f"text", True,(255,255,255))


    # screen.blit(background, (0, 0))
    

    # pygame.draw.polygon(canvas, (160,160,160), coordinates)
    pygame.draw.polygon(canvas, (255,0,0), shapes[0])
    pygame.draw.polygon(canvas, (0,255,0), shapes[1])
    pygame.draw.polygon(canvas, (0,0,255), shapes[2])

    screen.blit(background,(0,0))
    screen.blit(canvas, (50,75))
    screen.blit(text,(30,30))

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
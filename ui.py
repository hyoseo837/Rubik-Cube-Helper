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

colors = [(250, 65, 177),(6, 186, 227),(114, 32, 191),(99, 181, 30),(48, 104, 90),(235, 32, 143)]

color = [1,1,1,4,4,4,1,1,1]

coordinates = [(275,50),(405,125),(405,275),(275,350),(145,275),(145,125)]
# shapes = [[(405,125),(405,275),(275,350),(275,200)],[(275,350),(145,275),(145,125),(275,200)],[(145,125),(275,50),(405,125),(275,200)]]
UP_colors = [[(275,50),(318,75),(275,100),(232,75)],[(232,75),(275,100),(232,125),(188,100)],[(318,75),(362,100),(318,125),(275,100)]
,[(188,100),(232,125),(188,150),(145,125)],[(275,100),(318,125),(275,150),(232,125)],[(362,100),(405,125),(362,150),(318,125)]
,[(232,125),(275,150),(232,175),(188,150)],[(318,125),(362,150),(318,175),(275,150)],[(275,150),(318,175),(275,200),(232,175)]]
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
    for i in range(9):
        pygame.draw.polygon(canvas, colors[color[i]], UP_colors[i])

    screen.blit(background,(0,0))
    screen.blit(canvas, (50,75))
    screen.blit(text,(30,30))

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
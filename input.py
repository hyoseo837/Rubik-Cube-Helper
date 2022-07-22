import pygame
from ui_classes import button


def export():
    data = ""
    return data


pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Rubik's Cube Helper _ input")

clock = pygame.time.Clock()

submit = button("Submit", (470,330), 100, 40)
submit.setImage("images/submit.png")

# load background image
background = pygame.image.load("images/input_background.png")

# Text Variable
# [Font Name] = pygame.font.Font([Font Name], [Font Size])

# event loop
running = True
while running:

    dt = clock.tick(30)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if submit.check(mouse):
                running = False
                export()
        

    # Draw in Screen
    # Draw background
    screen.blit(background, (0, 0))
    screen.blit(submit.image, submit.pos)
    
    # Draw Sprite
    # screen.blit([Sprite Name], ([Sprite Coordinate]))
    
    # Draw Text
    # screen.blit([Text Name],([Text Coordinate]))

    # Update Screen
    pygame.display.update() 

# end game 
pygame.quit()
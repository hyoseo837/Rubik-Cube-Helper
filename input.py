import pygame
from ui_classes import button, colors

coordinates = [(190,45),(80,155),(190,155),(300,155),(410,155),(190,265)]

class face(button):
    def __init__(self,id,color,pos,fixed):
        self.size = (30,30)
        self.fixed = fixed
        self.pos = pos
        self.id = id
        self.color = color
        self.image = pygame.surface.Surface((28,28))
        pygame.draw.rect(self.image, colors[color], (0,0,28,28))

def export():
    pygame.init()

    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Rubik's Cube Helper _ input")

    clock = pygame.time.Clock()

    submit = button("Submit", (470,330), 100, 40)
    submit.setImage("images/submit.png")

    cube = []
    for i in range(6):
        for j in range(9):
            if j == 4:
                cube.append(face(9*i+j,i,(coordinates[i][0]+30*(j%3), coordinates[i][1]+30*(j//3)),True))
                continue
            cube.append(face(9*i+j,i,(coordinates[i][0]+30*(j%3), coordinates[i][1]+30*(j//3)),False))

    background = pygame.image.load("images/input_background.png")
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
                    result = ""
                    for i in cube:
                        result += str(i.color)
                    return result
                for i in cube:
                    if i.check(mouse) and i.fixed == False:
                        i.color = (i.color + 1) %6
                        pygame.draw.rect(i.image, colors[i.color], (0,0,28,28))

        screen.blit(background, (0, 0))
        for i in cube:
            screen.blit(i.image, i.pos)
        screen.blit(submit.image, submit.pos)
        
        pygame.display.update() 

    pygame.quit()
    
if __name__ == "__main__":
    print(export())
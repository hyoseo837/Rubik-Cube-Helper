import pygame
import os
location = os.path.dirname(os.path.abspath(__file__))
import cube_class

class Move_button():
    def __init__(self,moveID,pos,width,height):
        self.id = moveID
        self.text = MOVES[moveID]

        self.font = pygame.font.SysFont("Arial", 10)
        self.textSurf = self.font.render(self.text, 1, (255,255,255))
        self.image = pygame.Surface((width, height))
        pygame.draw.rect(self.image, (100,100,100), (0,0,width,height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        
        self.pos = pos

    def check(self,cdn):
        if cdn[0] > self.pos[0] and cdn[0] < self.pos[0] + 25 and cdn[1] > self.pos[1] and cdn[1] < self.pos[1] + 25:
            return True
        else: 
            return False


MOVES = ["U","u","D","d","L","l","R","r","F","f","B","b"]
cube = cube_class.cube()

pygame.init()

screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("cube solver")

clock = pygame.time.Clock()

aaFont = pygame.font.Font(None, 20)
background = pygame.image.load("images/background.png")

colors = [(230,230,230),(255, 88, 0),(0, 155, 72),(183, 18, 52),(0, 70, 173),(255, 213, 0)]

U_color = [0,0,0,0,0,0,0,0,0]
L_color = [0,0,0,0,0,0,0,0,0]
R_color = [0,0,0,0,0,0,0,0,0]

UP_colors = [[(275,50),(318,75),(275,100),(232,75)],[(318,75),(362,100),(318,125),(275,100)],[(362,100),(405,125),(362,150),(318,125)]
,[(232,75),(275,100),(232,125),(188,100)],[(275,100),(318,125),(275,150),(232,125)],[(318,125),(362,150),(318,175),(275,150)]
,[(188,100),(232,125),(188,150),(145,125)],[(232,125),(275,150),(232,175),(188,150)],[(275,150),(318,175),(275,200),(232,175)]]
LEFT_colors = [[(145,125),(188,150),(188,200),(145,175)],[(188,150),(232,175),(232,225),(188,200)],[(232,175),(275,200),(275,250),(232,225)],
[(145,175),(188,200),(188,250),(145,225)],[(188,200),(232,225),(232,275),(188,250)],[(232,225),(275,250),(275,300),(232,275)],
[(145,225),(188,250),(188,300),(145,275)],[(188,250),(232,275),(232,325),(188,300)],[(232,275),(275,300),(275,350),(232,325)]]
RIGHT_colors = [[(275,200),(318,175),(318,225),(275,250)],[(318,175),(362,150),(362,200),(318,225)],[(362,150),(405,125),(405,175),(362,200)],
[(275,250),(318,225),(318,275),(275,300)],[(318,225),(362,200),(362,250),(318,275)],[(362,200),(405,175),(405,225),(362,250)],
[(275,300),(318,275),(318,325),(275,350)],[(318,275),(362,250),(362,300),(318,325)],[(362,250),(405,225),(405,275),(362,300)]]



canvas = pygame.Surface((550,400))
buttonU = Move_button(0, (900,200), 30, 30)
buttonR = Move_button(6, (900,250), 30, 30)
buttonF = Move_button(8, (900,300), 30, 30)

running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if buttonU.check(mouse):
                cube.move(MOVES[buttonU.id])
            if buttonR.check(mouse):
                cube.move(MOVES[buttonR.id])
            if buttonF.check(mouse):
                cube.move(MOVES[buttonF.id])

    U_color = cube.colors[0:9]
    L_color = cube.colors[18:27]
    R_color = cube.colors[27:36]

    for i in range(9):
        U_color[i] = int(U_color[i])
        L_color[i] = int(L_color[i])
        R_color[i] = int(R_color[i])
    
    text = aaFont.render(f"text", True,(0,0,0))

    for i in range(9):
        pygame.draw.polygon(canvas, colors[U_color[i]], UP_colors[i])
        pygame.draw.polygon(canvas, (0,0,0), UP_colors[i],2)
        pygame.draw.polygon(canvas, colors[L_color[i]], LEFT_colors[i])
        pygame.draw.polygon(canvas, (0,0,0), LEFT_colors[i],2)
        pygame.draw.polygon(canvas, colors[R_color[i]], RIGHT_colors[i])
        pygame.draw.polygon(canvas, (0,0,0), RIGHT_colors[i],2)

    screen.blit(background,(0,0))
    screen.blit(buttonU.image, buttonU.pos)
    screen.blit(buttonF.image, buttonF.pos)
    screen.blit(buttonR.image, buttonR.pos)
    screen.blit(canvas, (50,75))
    screen.blit(text,(30,30))

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
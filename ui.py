import pygame
import os
location = os.path.dirname(os.path.abspath(__file__))
import cube_class

class button():
    def __init__(self,name,pos,width,height):
        self.name = name
        self.pos = pos
        self.size = [width,height]
        self.image = pygame.Surface((width,height))

    def setImage(self,path):
        self.image = pygame.image.load(path)
        
    def check(self,cdn):
        if cdn[0] > self.pos[0] and cdn[0] < self.pos[0] + self.size[0] and cdn[1] > self.pos[1] and cdn[1] < self.pos[1] + self.size[1]:
            return True
        else: 
            return False

class Move_button(button):
    def __init__(self,moveID,pos,width,height):
        super().__init__(moveID, pos, width, height)
        self.id = moveID
        self.text = MOVES[moveID]

        self.font = pygame.font.SysFont("Arial", 20)
        self.textSurf = self.font.render(self.text,1, (255,255,255))
        self.image = pygame.Surface((width, height))
        pygame.draw.rect(self.image, (100,100,100), (0,0,width,height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])



MOVES = ["U","u","D","d","L","l","R","r","F","f","B","b"]
cube = cube_class.cube()

pygame.init()

screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("cube solver")

clock = pygame.time.Clock()
background = pygame.image.load("images/background.png")

colors = [(230,230,230),(255, 88, 0),(0, 155, 72),(183, 18, 52),(0, 70, 173),(255, 213, 0)]
# coordinate data
UP_colors = [[(275,50),(318,75),(275,100),(232,75)],[(318,75),(362,100),(318,125),(275,100)],[(362,100),(405,125),(362,150),(318,125)]
,[(232,75),(275,100),(232,125),(188,100)],[(275,100),(318,125),(275,150),(232,125)],[(318,125),(362,150),(318,175),(275,150)]
,[(188,100),(232,125),(188,150),(145,125)],[(232,125),(275,150),(232,175),(188,150)],[(275,150),(318,175),(275,200),(232,175)]]
FRONT_colors = [[(145,125),(188,150),(188,200),(145,175)],[(188,150),(232,175),(232,225),(188,200)],[(232,175),(275,200),(275,250),(232,225)],
[(145,175),(188,200),(188,250),(145,225)],[(188,200),(232,225),(232,275),(188,250)],[(232,225),(275,250),(275,300),(232,275)],
[(145,225),(188,250),(188,300),(145,275)],[(188,250),(232,275),(232,325),(188,300)],[(232,275),(275,300),(275,350),(232,325)]]
RIGHT_colors = [[(275,200),(318,175),(318,225),(275,250)],[(318,175),(362,150),(362,200),(318,225)],[(362,150),(405,125),(405,175),(362,200)],
[(275,250),(318,225),(318,275),(275,300)],[(318,225),(362,200),(362,250),(318,275)],[(362,200),(405,175),(405,225),(362,250)],
[(275,300),(318,275),(318,325),(275,350)],[(318,275),(362,250),(362,300),(318,325)],[(362,250),(405,225),(405,275),(362,300)]]
DOWN_colors = [[(446,342),(461,350),(446,358),(432,350)],[(461,350),(475,358),(461,367),(446,358)],[(475,358),(489,367),(475,375),(461,367)]
,[(461,334),(475,342),(461,350),(446,342)],[(475,342),(489,350),(475,358),(461,350)],[(489,350),(504,358),(489,367),(475,358)]
,[(475,325),(489,334),(475,342),(461,334)],[(489,334),(504,342),(489,350),(475,342)],[(504,342),(518,350),(504,358),(489,350)]]
BACK_colors = [[(504,292),(518,300),(518,317),(504,308)],[(489,283),(504,292),(504,308),(489,300)],[(475,275),(489,283),(489,300),(475,292)]
,[(504,308),(518,317),(518,334),(504,325)],[(489,300),(504,308),(504,325),(489,317)],[(475,292),(489,300),(489,317),(475,308)]
,[(504,325),(518,334),(518,350),(504,342)],[(489,317),(504,325),(504,342),(489,334)],[(475,308),(489,317),(489,334),(475,325)]]
LEFT_colors = [[(461,283),(475,275),(475,292),(461,300)],[(446,292),(461,283),(461,300),(446,308)],[(432,300),(446,292),(446,308),(432,317)]
,[(461,300),(475,292),(475,308),(461,317)],[(446,308),(461,300),(461,317),(446,325)],[(432,317),(446,308),(446,325),(432,334)]
,[(461,317),(475,308),(475,325),(461,334)],[(446,325),(461,317),(461,334),(446,342)],[(432,334),(446,325),(446,342),(432,350)]]



viewButton = button("Viewbutton", (60,85), 30, 30)
viewButton.setImage("images/viewButton.png")

buttons = []
for i in range(12):
    buttons.append(Move_button(i,(610+(i//2)*50,150+50*(i%2)),40,40))

viewmod = 0

running = True
while running:

    dt = clock.tick(60)
    cubeCanvas = pygame.Surface((550,400))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for button in buttons:
                if button.check(mouse):
                    cube.move(MOVES[button.id])
            if viewButton.check(mouse):
                viewmod = (viewmod + 1)%2;

    U_color = cube.colors[0:9]
    L_color = cube.colors[9:18]
    F_color = cube.colors[18:27]
    R_color = cube.colors[27:36]
    B_color = cube.colors[36:45]
    D_color = cube.colors[45:54]

    for i in range(9):
        U_color[i] = int(U_color[i])
        L_color[i] = int(L_color[i])
        F_color[i] = int(F_color[i])
        R_color[i] = int(R_color[i])
        D_color[i] = int(D_color[i])
        B_color[i] = int(B_color[i])
    

    if viewmod == 0: # 3D
        for i in range(9):
            pygame.draw.polygon(cubeCanvas, colors[U_color[i]], UP_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), UP_colors[i],2)
            pygame.draw.polygon(cubeCanvas, colors[L_color[i]], LEFT_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), LEFT_colors[i],2)
            pygame.draw.polygon(cubeCanvas, colors[F_color[i]], FRONT_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), FRONT_colors[i],2)
            pygame.draw.polygon(cubeCanvas, colors[R_color[i]], RIGHT_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), RIGHT_colors[i],2)
            pygame.draw.polygon(cubeCanvas, colors[D_color[i]], DOWN_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), DOWN_colors[i],2)
            pygame.draw.polygon(cubeCanvas, colors[B_color[i]], BACK_colors[i])
            pygame.draw.polygon(cubeCanvas, (0,0,0), BACK_colors[i],2)
            pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (475,375),width=3)
            pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (432,300),width=3)
            pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (518,300),width=3)
    else:
        for i in range(9):
            pygame.draw.polygon(cubeCanvas, colors[U_color[i]], [(175+30*(i%3), 45+30*(i//3)),(205+30*(i%3), 45+30*(i//3)),(205+30*(i%3), 75+30*(i//3)),(175+30*(i%3), 75+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(175+30*(i%3), 45+30*(i//3)),(205+30*(i%3), 45+30*(i//3)),(205+30*(i%3), 75+30*(i//3)),(175+30*(i%3), 75+30*(i//3))],2)

            pygame.draw.polygon(cubeCanvas, colors[L_color[i]], [(65+30*(i%3), 155+30*(i//3)),(95+30*(i%3), 155+30*(i//3)),(95+30*(i%3), 185+30*(i//3)),(65+30*(i%3), 185+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(65+30*(i%3), 155+30*(i//3)),(95+30*(i%3), 155+30*(i//3)),(95+30*(i%3), 185+30*(i//3)),(65+30*(i%3), 185+30*(i//3))],2)

            pygame.draw.polygon(cubeCanvas, colors[F_color[i]], [(175+30*(i%3), 155+30*(i//3)),(205+30*(i%3), 155+30*(i//3)),(205+30*(i%3), 185+30*(i//3)),(175+30*(i%3), 185+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(175+30*(i%3), 155+30*(i//3)),(205+30*(i%3), 155+30*(i//3)),(205+30*(i%3), 185+30*(i//3)),(175+30*(i%3), 185+30*(i//3))],2)

            pygame.draw.polygon(cubeCanvas, colors[R_color[i]], [(285+30*(i%3), 155+30*(i//3)),(315+30*(i%3), 155+30*(i//3)),(315+30*(i%3), 185+30*(i//3)),(285+30*(i%3), 185+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(285+30*(i%3), 155+30*(i//3)),(315+30*(i%3), 155+30*(i//3)),(315+30*(i%3), 185+30*(i//3)),(285+30*(i%3), 185+30*(i//3))],2)

            pygame.draw.polygon(cubeCanvas, colors[B_color[i]], [(395+30*(i%3), 155+30*(i//3)),(425+30*(i%3), 155+30*(i//3)),(425+30*(i%3), 185+30*(i//3)),(395+30*(i%3), 185+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(395+30*(i%3), 155+30*(i//3)),(425+30*(i%3), 155+30*(i//3)),(425+30*(i%3), 185+30*(i//3)),(395+30*(i%3), 185+30*(i//3))],2)

            pygame.draw.polygon(cubeCanvas, colors[D_color[i]], [(175+30*(i%3), 265+30*(i//3)),(205+30*(i%3), 265+30*(i//3)),(205+30*(i%3), 295+30*(i//3)),(175+30*(i%3), 295+30*(i//3))])
            pygame.draw.polygon(cubeCanvas, (0,0,0), [(175+30*(i%3), 265+30*(i//3)),(205+30*(i%3), 265+30*(i//3)),(205+30*(i%3), 295+30*(i//3)),(175+30*(i%3), 295+30*(i//3))],2)

    screen.blit(background,(0,0))
    for button in buttons:
        screen.blit(button.image, button.pos)
    screen.blit(cubeCanvas, (50,75))
    screen.blit(viewButton.image, viewButton.pos)

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
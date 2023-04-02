import pygame
import os
location = os.path.dirname(os.path.abspath(__file__))
import cube_class
from ui_classes import *
from input import export
from mysolver import mysolve

cube = cube_class.Cube()

pygame.init()

screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("cube solver")

clock = pygame.time.Clock()
solution = []
page = 0;
background = pygame.image.load("images/background.png")

COORDINATE_DATA = \
[[(275, 50),(318, 75),(275,100),(232, 75)],[(318, 75),(362,100),(318,125),(275,100)],
[(362,100),(405,125),(362,150),(318,125)],[(232, 75),(275,100),(232,125),(188,100)],
[(275,100),(318,125),(275,150),(232,125)],[(318,125),(362,150),(318,175),(275,150)],
[(188,100),(232,125),(188,150),(145,125)],[(232,125),(275,150),(232,175),(188,150)],
[(275,150),(318,175),(275,200),(232,175)],[(461,283),(475,275),(475,292),(461,300)],
[(446,292),(461,283),(461,300),(446,308)],[(432,300),(446,292),(446,308),(432,317)],
[(461,300),(475,292),(475,308),(461,317)],[(446,308),(461,300),(461,317),(446,325)],
[(432,317),(446,308),(446,325),(432,334)],[(461,317),(475,308),(475,325),(461,334)],
[(446,325),(461,317),(461,334),(446,342)],[(432,334),(446,325),(446,342),(432,350)],
[(145,125),(188,150),(188,200),(145,175)],[(188,150),(232,175),(232,225),(188,200)],
[(232,175),(275,200),(275,250),(232,225)],[(145,175),(188,200),(188,250),(145,225)],
[(188,200),(232,225),(232,275),(188,250)],[(232,225),(275,250),(275,300),(232,275)],
[(145,225),(188,250),(188,300),(145,275)],[(188,250),(232,275),(232,325),(188,300)],
[(232,275),(275,300),(275,350),(232,325)],[(275,200),(318,175),(318,225),(275,250)],
[(318,175),(362,150),(362,200),(318,225)],[(362,150),(405,125),(405,175),(362,200)],
[(275,250),(318,225),(318,275),(275,300)],[(318,225),(362,200),(362,250),(318,275)],
[(362,200),(405,175),(405,225),(362,250)],[(275,300),(318,275),(318,325),(275,350)],
[(318,275),(362,250),(362,300),(318,325)],[(362,250),(405,225),(405,275),(362,300)],
[(504,292),(518,300),(518,317),(504,308)],[(489,283),(504,292),(504,308),(489,300)],
[(475,275),(489,283),(489,300),(475,292)],[(504,308),(518,317),(518,334),(504,325)],
[(489,300),(504,308),(504,325),(489,317)],[(475,292),(489,300),(489,317),(475,308)],
[(504,325),(518,334),(518,350),(504,342)],[(489,317),(504,325),(504,342),(489,334)],
[(475,308),(489,317),(489,334),(475,325)],[(446,342),(461,350),(446,358),(432,350)],
[(461,350),(475,358),(461,367),(446,358)],[(475,358),(489,367),(475,375),(461,367)],
[(461,334),(475,342),(461,350),(446,342)],[(475,342),(489,350),(475,358),(461,350)],
[(489,350),(504,358),(489,367),(475,358)],[(475,325),(489,334),(475,342),(461,334)],
[(489,334),(504,342),(489,350),(475,342)],[(504,342),(518,350),(504,358),(489,350)]]


PLANNER_DATA = [(175,45),(65,155),(175,155),(285,155),(395,155),(175,265)]


viewButton = button("viewbutton", (60,85), 30, 30)
viewButton.setImage("images/viewButton.png")
importButton = button("importButton", (60,435), 30, 30)
importButton.setImage("images/importButton.png")

aafont = pygame.font.SysFont("Helvetica", 17)

turn_Buttons = []
turn_Buttons.append(button("turnX", (500,85), 20, 20))
turn_Buttons.append(button("turnY", (530,85), 20, 20))
turn_Buttons.append(button("turnZ", (560,85), 20, 20))
turn_Buttons[0].setImage("images/turnX.png")
turn_Buttons[1].setImage("images/turnY.png")
turn_Buttons[2].setImage("images/turnZ.png")

output_button = button("output", (560,435), 30, 30)
output_button.setImage("images/outputButton.png")

buttons = []
for i in range(12):
    buttons.append(Move_button(i,(620+(i//2)*60,85+50*(i%2)),40,40))

viewmod = 0
shift = False
running = True
while running:

    dt = clock.tick(60)
    cubeCanvas = pygame.Surface((550,400))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            # print(mouse)
            if mouse[0] > 830 and mouse[0] < 940 and mouse[1] > 310 and mouse[1] < 325:
                solution = mysolve(cube.save())
                page = 0
            if mouse[0] > 650 and mouse[0] < 670 and mouse[1] > 450 and mouse[1] < 470:
                if page != 0:
                    page -= 1
            if mouse[0] > 930 and mouse[0] < 950 and mouse[1] > 450 and mouse[1] < 470:
                if len(solution) > (page+1)*68:
                    page += 1
            for button in buttons:
                if button.pressed(mouse):
                    cube.move(MOVES[button.id])
            if viewButton.pressed(mouse):
                viewmod = (viewmod + 1)%2;
            if importButton.pressed(mouse):
                cube = cube_class.Cube(export())
                pygame.display.set_mode((screen_width,screen_height))
            if output_button.pressed(mouse):
                print(cube.save())
            if turn_Buttons[0].pressed(mouse):
                cube.move("X")
            if turn_Buttons[1].pressed(mouse):
                cube.move("Y")
            if turn_Buttons[2].pressed(mouse):
                cube.move("Z")
        

    display_color = [int(x) for x in cube.colors]
    
    solution_background = pygame.image.load("images/Solution_screen.png")
    solution_text = aafont.render("  ".join(solution[page*68:page*68+17]), 1, (0,0,0))
    solution_background.blit(solution_text, (15,45))
    if len(solution)> 15:
        solution_text = aafont.render("  ".join(solution[page*68+17:page*68+34]), 1, (0,0,0))
        solution_background.blit(solution_text, (15,70))
        if len(solution)> 30:
            solution_text = aafont.render("  ".join(solution[page*68+34:page*68+51]), 1, (0,0,0))
            solution_background.blit(solution_text, (15,95))
            if len(solution)> 45:
                solution_text = aafont.render("  ".join(solution[page*68+51:page*68+68]), 1, (0,0,0))
                solution_background.blit(solution_text, (15,120))

    if viewmod == 0: # 3D
        for x in range(6):
            for i in range(9):
                pygame.draw.polygon(cubeCanvas, colors[display_color[9*x+i]], COORDINATE_DATA[9*x+i])
                pygame.draw.polygon(cubeCanvas, (0,0,0), COORDINATE_DATA[9*x+i],2)
        pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (475,375),width=3)
        pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (432,300),width=3)
        pygame.draw.line(cubeCanvas, (10,10,10), (475,325), (518,300),width=3)
    else:
        for x in range(6):
            for i in range(9):
                pygame.draw.polygon(cubeCanvas, colors[display_color[9*x + i]],
                [(PLANNER_DATA[x][0]+30*(i%3), PLANNER_DATA[x][1]+30*(i//3)),(PLANNER_DATA[x][0]+30+30*(i%3), PLANNER_DATA[x][1]+30*(i//3)),
                (PLANNER_DATA[x][0]+30+30*(i%3), PLANNER_DATA[x][1]+30+30*(i//3)),(PLANNER_DATA[x][0]+30*(i%3), PLANNER_DATA[x][1]+30+30*(i//3))])
                pygame.draw.polygon(cubeCanvas, (0,0,0),
                [(PLANNER_DATA[x][0]+30*(i%3), PLANNER_DATA[x][1]+30*(i//3)),(PLANNER_DATA[x][0]+30+30*(i%3), PLANNER_DATA[x][1]+30*(i//3)),
                (PLANNER_DATA[x][0]+30+30*(i%3), PLANNER_DATA[x][1]+30+30*(i//3)),(PLANNER_DATA[x][0]+30*(i%3), PLANNER_DATA[x][1]+30+30*(i//3))],2)
            
    screen.blit(background,(0,0))
    for button in buttons:
        screen.blit(button.image, button.pos)
    screen.blit(cubeCanvas, (50,75))
    screen.blit(solution_background, (650,300))
    screen.blit(viewButton.image, viewButton.pos)
    screen.blit(importButton.image, importButton.pos)
    screen.blit(output_button.image, output_button.pos)
    for button in turn_Buttons:
        screen.blit(button.image, button.pos)

    # Update Screen
    pygame.display.update()

# pause
pygame.time.delay(200)

# end game 
pygame.quit()
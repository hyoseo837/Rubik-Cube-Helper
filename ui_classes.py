import pygame

MOVES = ["U","u","D","d","L","l","R","r","F","f","B","b"]
colors = [(230,230,230),(255, 88, 0),(0, 155, 72),(183, 18, 52),(0, 70, 173),(255, 213, 0)]
color_order = [0,5,1,3,2,4]

class button():
    def __init__(self,name,pos,width,height):
        self.name = name
        self.pos = pos
        self.size = (width,height)
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
        self.image = pygame.image.load(f"images/move{self.id%2}.png")
        pygame.draw.circle(self.image, colors[color_order[self.id//2]], (20,20), 16,3)


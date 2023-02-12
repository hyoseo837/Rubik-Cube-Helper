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
        
    def pressed(self,cdn):
        if cdn[0] > self.pos[0] and cdn[0] < self.pos[0] + self.size[0] and cdn[1] > self.pos[1] and cdn[1] < self.pos[1] + self.size[1]:
            return True
        else: 
            return False

class Move_button(button):
    def __init__(self,moveID,pos,width,height):
        super().__init__(moveID, pos, width, height)
        self.id = moveID
        self.text = MOVES[moveID]

        self.font = pygame.font.SysFont("Arial", 15)
        self.textSurf = self.font.render(self.text,1, (255,255,255))
        self.image = pygame.Surface((width, height))
        pygame.draw.rect(self.image, (100,100,100), (0,0,width,height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

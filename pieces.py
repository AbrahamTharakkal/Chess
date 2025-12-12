import pygame
from constants import *
class Pieces(pygame.sprite.Sprite):
    char_lst = ['a','b','c','d','e','f','g','h']
    def __init__(self,piece,col_num,row_char,color,ID):
        super().__init__()
        self.piece = piece
        self.color = color
        if self.color == (255,255,255):
            self.color_str = 'WHITE'
        else:
            self.color_str = 'BLACK'
        self.id = ID
        self.col_num = col_num
        self.row_char = row_char
        self.image = pygame.Surface((75,75))
        self.image.fill(LIGHTGREEN)
        self.image.set_colorkey(LIGHTGREEN)
        self.rect = self.image.get_rect()
        self.rect.x = Pieces.char_lst.index(self.row_char) * 75
        self.rect.y = (int(self.col_num)-1) * 75
        self.chosen = False
        if self.piece == 'p':
            pygame.draw.polygon(self.image,self.color,((0,75),(75,75),(75,0)))
        if self.piece == 'r':
            pygame.draw.rect(self.image,self.color,(0,0,60,60))
        if self.piece == 'b':
            pygame.draw.ellipse(self.image,self.color,(3,3,69,69),5)
        if self.piece == 'q':
            pygame.draw.ellipse(self.image,self.color,(0,0,75,75))
        if self.piece == 'k':
            pygame.draw.rect(self.image,self.color,(0,0,75,75))
        if self.piece == 'n':
            pygame.draw.circle(self.image,self.color,(37,37),37,0,False,True,True,True)
    def find_pos(self,mx,my):
        for pos in POSITIONS:
            if mx >= POSITIONS[pos][0] and mx <= POSITIONS[pos][2] and my >= POSITIONS[pos][1] and my <= POSITIONS[pos][3]:
                row_char = pos[0]
                col_num = int(pos[1])
        return row_char + str(col_num)
    def move(self,new_char,new_col):
        self.rect.x = Pieces.char_lst.index(new_char) * 75
        self.rect.y = (int(new_col)-1) * 75
    def ID(self,mx,my):
        if (mx >= self.rect.x and mx <= self.rect.x + 75) and (my >= self.rect.y and my <= self.rect.y +75):
            # print('taken',mx,my)
            return True
        else:
            # print('open',mx,my)
            return False
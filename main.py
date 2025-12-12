import sys
import pygame
from pygame.locals import QUIT
from constants import *
from pieces import Pieces

SCREEN_SIZE[0] = 600
SCREEN_SIZE[1] = 600

pygame.init()

DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Chess.com')
all_sprites = pygame.sprite.Group()
white_sprites = pygame.sprite.Group()
black_sprites = pygame.sprite.Group()
pieces = []

colors = [(139,69,19),(82, 47, 30)]

for i in range(8):
    for j in range(8):
        pygame.draw.rect(DISPLAYSURF, colors[(j+i)%2], (75*j,75*i,75,75))

# pawn = Pieces('p',2,'a',WHITE,1)
# bishop = Pieces('b',1,'c',WHITE,1)
# knight = Pieces('n',1,'b',WHITE,1)
# rook = Pieces('r',1,'a',WHITE,1)
# queen = Pieces('q',1,'d',WHITE,1)
# king = Pieces('k',1,,'e'WHITE,1)

def reset():
  # -------------------------WHITE SETUP--------------------------
  for i in range(8):
    piece = Pieces('p',7,Pieces.char_lst[i],WHITE,i+1)
    all_sprites.add(piece)
    white_sprites.add(piece)
  rook1 = Pieces('r',8,'a',WHITE,1)
  rook2 = Pieces('r',8,'h',WHITE,2)
  knight1 = Pieces('n',8,'b',WHITE,1)
  knight2 = Pieces('n',8,'g',WHITE,2)
  bishop1 = Pieces('b',8,'c',WHITE,1)
  bishop2 = Pieces('b',8,'f',WHITE,2)
  queen = Pieces('q',8,'d',WHITE,1)
  king = Pieces('k',8,'e',WHITE,1)
  all_sprites.add(rook1)
  all_sprites.add(rook2)
  all_sprites.add(knight1)
  all_sprites.add(knight2)
  all_sprites.add(bishop1)
  all_sprites.add(bishop2)
  all_sprites.add(king)
  all_sprites.add(queen)
  white_sprites.add(rook1)
  white_sprites.add(rook2)
  white_sprites.add(knight1)
  white_sprites.add(knight2)
  white_sprites.add(bishop1)
  white_sprites.add(bishop2)
  white_sprites.add(king)
  white_sprites.add(queen)
  # -------------------------WHITE SETUP--------------------------
  # -------------------------BLACK SETUP--------------------------
  for i in range(8):
    piece = Pieces('p',2,Pieces.char_lst[i],BLACK,i+1)
    all_sprites.add(piece)
    black_sprites.add(piece)
  rook1B = Pieces('r',1,'a',BLACK,1)
  rook2B = Pieces('r',1,'h',BLACK,2)
  knight1B = Pieces('n',1,'b',BLACK,1)
  knight2B = Pieces('n',1,'g',BLACK,2)
  bishop1B = Pieces('b',1,'c',BLACK,1)
  bishop2B = Pieces('b',1,'f',BLACK,2)
  queenB = Pieces('q',1,'d',BLACK,1)
  kingB = Pieces('k',1,'e',BLACK,1)
  all_sprites.add(rook1B)
  all_sprites.add(rook2B)
  all_sprites.add(knight1B)
  all_sprites.add(knight2B)
  all_sprites.add(bishop1B)
  all_sprites.add(bishop2B)
  all_sprites.add(kingB)
  all_sprites.add(queenB)
  black_sprites.add(rook1B)
  black_sprites.add(rook2B)
  black_sprites.add(knight1B)
  black_sprites.add(knight2B)
  black_sprites.add(bishop1B)
  black_sprites.add(bishop2B)
  black_sprites.add(kingB)
  black_sprites.add(queenB)
  for sprite in black_sprites:
    pieces.append(sprite)
  for sprite in white_sprites:
    pieces.append(sprite)
  # -------------------------BLACK SETUP--------------------------

flag = 0
mouse_square = None
reset()
chosen = None
taken = False
can_move = False
destination = [None,None]
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        mousepos = [mouseX,mouseY]
        if flag == 1:
          taken = False
          for piece in pieces:
            if piece.ID(mouseX,mouseY):
              can_move = False
              taken = True
              flag = 0
              chosen = None
              break
          if not taken:
            taken = False
            can_move = True
            mouse_square = (piece.find_pos(mouseX,mouseY), piece.color_str, piece.piece, piece.id)
            piece.row_char = mouse_square[0][0]
            piece.col_num = int(mouse_square[0][1])
            destination = [mouse_square[0][0],int(mouse_square[0][1])]
            # print('open',mouse_square)
        elif flag == 0:
          for piece in pieces:
            if piece.ID(mouseX,mouseY):
              flag = 1
              if not chosen:
                chosen = piece
                chosen.chosen = True
              mouse_square = (piece.row_char + str(piece.col_num), piece.color_str, piece.piece, piece.id)
              # print('taken',mouse_square)
  if chosen and can_move:
    print(chosen.chosen, chosen.row_char + str(chosen.col_num), chosen.color_str, chosen.piece, chosen.id)
    chosen.move(destination[0],destination[1])
    flag = 0
    chosen = None
    can_move = False
  for i in range(8):
    for j in range(8):
        pygame.draw.rect(DISPLAYSURF, colors[(j+i)%2], (75*j,75*i,75,75))
  all_sprites.draw(DISPLAYSURF)
  pygame.display.update()
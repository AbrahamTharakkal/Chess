import sys
import pygame
from pygame.locals import QUIT
from constants import *
from pieces import Pieces
import chess

board = chess.Board()

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
  # ------------------------- BLACK SETUP--------------------------
  for i in range(8):
    piece = Pieces('p',7,Pieces.char_lst[i],BLACK,i+1)
    all_sprites.add(piece)
    black_sprites.add(piece)
  rook1 = Pieces('r',8,'a',BLACK,1)
  rook2 = Pieces('r',8,'h',BLACK,2)
  knight1 = Pieces('n',8,'b',BLACK,1)
  knight2 = Pieces('n',8,'g',BLACK,2)
  bishop1 = Pieces('b',8,'c',BLACK,1)
  bishop2 = Pieces('b',8,'f',BLACK,2)
  queen = Pieces('q',8,'d',BLACK,1)
  king = Pieces('k',8,'e',BLACK,1)
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
  # -------------------------BLACK SETUP--------------------------
  # -------------------------WHITE SETUP--------------------------
  for i in range(8):
    piece = Pieces('p',2,Pieces.char_lst[i],WHITE,i+1)
    all_sprites.add(piece)
    white_sprites.add(piece)
  rook1B = Pieces('r',1,'a',WHITE,1)
  rook2B = Pieces('r',1,'h',WHITE,2)
  knight1B = Pieces('n',1,'b',WHITE,1)
  knight2B = Pieces('n',1,'g',WHITE,2)
  bishop1B = Pieces('b',1,'c',WHITE,1)
  bishop2B = Pieces('b',1,'f',WHITE,2)
  queenB = Pieces('q',1,'d',WHITE,1)
  kingB = Pieces('k',1,'e',WHITE,1)
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
  # -------------------------WHITE SETUP--------------------------

flag = 0
mouse_square = None
reset()
chosen = None
taken = False
can_move = False
destination = [None,None]
old_pos = None
turn_count = 0
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
          # old_pos = None
          taken = False
          chosen.taking = False
          for piece in pieces:
            if piece.ID(mouseX,mouseY):
              if chosen.check(board,chosen.find_pos(mouseX,mouseY)[0],chosen.find_pos(mouseX,mouseY)[1]):
                taken = False
                can_move = True

                # old_pos = piece.find_pos(mouseX,mouseY)

                mouse_square = (chosen.find_pos(mouseX,mouseY), chosen.color_str, chosen.piece, chosen.id)
                chosen.row_char = mouse_square[0][0]
                chosen.col_num = int(mouse_square[0][1])
                destination = [mouse_square[0][0],int(mouse_square[0][1])]
                for piece in pieces:
                  if piece.row_char == mouse_square[0][0] and piece.col_num == int(mouse_square[0][1]):
                    all_sprites.remove(piece)
                    chosen.taking = True
                    if piece.color_str == "WHITE":
                      white_sprites.remove(piece)
                    else:
                      black_sprites.remove(piece)
                    pieces.pop(pieces.index(piece))
                    piece.eliminate()
                    break
                break
              else:
                can_move = False
                taken = True
                flag = 0
                chosen.taking = False
                chosen = None
                break
          if not taken:
            print(chosen.check(board,chosen.find_pos(mouseX,mouseY)[0],chosen.find_pos(mouseX,mouseY)[1]))
            print(chosen.color_str,chosen.piece,chosen.find_pos(mouseX,mouseY)[0],chosen.find_pos(mouseX,mouseY)[1])
            if chosen.check(board,chosen.find_pos(mouseX,mouseY)[0],chosen.find_pos(mouseX,mouseY)[1]):
              taken = False
              chosen.taking = False
              can_move = True

              # old_pos = piece.find_pos(mouseX,mouseY)

              mouse_square = (chosen.find_pos(mouseX,mouseY), chosen.color_str, chosen.piece, chosen.id)
              chosen.row_char = mouse_square[0][0]
              chosen.col_num = int(mouse_square[0][1])
              destination = [mouse_square[0][0],int(mouse_square[0][1])]
            # print('open',mouse_square)
        elif flag == 0:
          old_pos = None
          for piece in pieces:
            if turn_count % 2 == 0 and piece.color_str == 'WHITE' or turn_count % 2 == 1 and piece.color_str == 'BLACK':
              if piece.ID(mouseX,mouseY):
                flag = 1
                old_pos = piece.find_pos(mouseX,mouseY)
                if not chosen:
                  chosen = piece
                  chosen.chosen = True
                mouse_square = (piece.row_char + str(piece.col_num), piece.color_str, piece.piece, piece.id)
                # print('taken',mouse_square)
  if chosen and can_move:
    print(chosen.chosen, chosen.row_char + str(chosen.col_num), chosen.color_str, chosen.piece, chosen.id)
    # if piece.color_str == 'WHITE':
    print(destination[0]+str(destination[1]))
    if chosen.piece == 'p':
      if chosen.taking:
        board.push_san(old_pos[0][0]+'x'+destination[0]+str(destination[1]))
        old_pos = None
      else:
        board.push_san(destination[0]+str(destination[1]))
    else:
      board.push_san(chosen.piece.upper()+destination[0]+str(destination[1]))
    print(board)
    chosen.move(destination[0],destination[1])
    flag = 0
    chosen.taking = False
    chosen = None
    can_move = False
    turn_count += 1
    print(turn_count)
    print(' ')
  for i in range(8):
    for j in range(8):
        pygame.draw.rect(DISPLAYSURF, colors[(j+i)%2], (75*j,75*i,75,75))
  all_sprites.draw(DISPLAYSURF)
  pygame.display.update()
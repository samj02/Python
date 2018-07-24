import pygame
import sys

from pygame.locals import *


pygame.init()

tie = 0
turn = True

gim=pygame.image.load("images/TTTBoard.png")
O=pygame.image.load("images/TTTO.png")
X=pygame.image.load("images/TTTX.png")
gim=pygame.transform.scale(gim, (450,450))
X=pygame.transform.scale(X, (400,400))
O=pygame.transform.scale(O, (400,400))

screen = pygame.display.set_mode((700, 500))
screen.blit(gim, (100, 100))
screen.blit(X, (100, 100))
screen.blit(O, (100, 100))

positions_groups = (
    [[(x, y) for y in range(3)] for x in range(3)] +
    [[(x, y) for x in range(3)] for y in range(3)] +
    [[(d, d) for d in range(3)]] +
    [[(2-d, d) for d in range(3)]]
)

def get_winner(board):
    """Return winner piece in board (None if no winner)."""
    for positions in positions_groups:
        values = [board[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0]:
            return values[0]

board = [
    ["x", "x", "x"],
    ["x", "x", "x"],
    ["x", "x", "x"],
]

print(get_winner(board)) # "X"

circles = []

cord=[(-80,-125), (70, -125), (210, -125), (-80, 25), (70, 25), (210, 25), (-80, 175), (70, 175), (210, 175)]

screen.fill((255, 255, 255))

for circle in circles:
    circle = pygame.draw.circle((screen), (0, 0, 0),(mouse_x, mouse_y), 15, 2)

font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('TicTacToe')


def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)
def draw_screen():
    screen.fill((255, 255, 255))
    screen.blit(gim, (50, 0))
draw_screen()
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.quit

count=0
main_clock = pygame.time.Clock()


def draw_moves():
    for x in range(0,3):
        for y in range(0,3):
            if board[x][y]=="X":
                screen.blit(X,cord[x*3+y])
            elif board[x][y]=="O":
                screen.blit(O, cord[x*3+y])



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            count+=1


            (mouse_x, mouse_y )= pygame.mouse.get_pos()

            if mouse_y >0 and mouse_y <150:
                if mouse_x >50 and mouse_x < 190:
                    if board[0][0]== "X" or board[0][0]=="O":
                        print("This space is taken!")
                        count-=1

                    elif turn == True:
                            board[0][0]="X"
                            screen.blit(X, cord[0])
                            tie += 1 
                            

                    else:
                        board[0][0]="O"
                        screen.blit(O, cord[0])
                        tie += 1 


                if mouse_x >190 and mouse_x <343:
                    if board[0][1]=="X" or board[0][1]=="O":
                        print("This space is taken!")
                        count-=1
                    elif turn == True:
                        board[0][1]="X"
                        screen.blit(X, cord[1])
                        tie += 1 

                    else:
                        board[0][1]="O"
                        screen.blit(O, cord[1])
                        tie += 1 




                if mouse_x >343 and mouse_x <500:

                     if board[0][2]=="X" or board[0][2]=="O":
                        print("This space is taken!")
                        count-=1
                     elif turn == True:
                        board[0][2]="X"
                        screen.blit(X, cord[2])
                        tie += 1 
                     else:
                        board[0][2]="O"
                        screen.blit(O, cord[2])
                        tie += 1 
            if mouse_y >150 and mouse_y <300:
                if mouse_x >50 and mouse_x < 190:
                    if board[1][0]=="X" or board[1][0]=="O":
                        print("This space is taken!")
                        count-=1
                    elif turn == True:
                        board[1][0]="X"
                        screen.blit(X, cord[3])
                        tie += 1 
                    else:
                        board[1][0]="O"
                        screen.blit(O, cord[3])
                        tie += 1 


                if mouse_x >190 and mouse_x <343:
                    if board[1][1]=="X" or board[1][1]=="O":
                        print("This space is taken!")
                        count-=1

                    elif turn == True:
                        board[1][1]="X"
                        screen.blit(X, cord[4])
                        tie += 1 
                    else:
                        board[1][1]="O"
                        screen.blit(O, cord[4])
                        tie += 1 

                if mouse_x >343 and mouse_x <500:
                    if board[1][2]=="X" or board[1][2]=="O":
                        print("This space is taken!")
                        count-=1

                    elif turn == True:
                        board[1][2]="X"
                        screen.blit(X, cord[5])
                        tie += 1 
                    else:
                        board[1][2]="O"
                        screen.blit(O, cord[5])
                        tie += 1 
            if mouse_y >300 and mouse_y<450:
                if mouse_x >50 and mouse_x < 190:
                    if board[2][0]=="X" or board[2][0]=="O":
                        print("This space is taken! ")
                        count-=1
                    elif turn == True:
                        board[2][0]="X"
                        screen.blit(X, cord[6])
                        tie += 1 
                    else:
                        board[2][0]="O"
                        screen.blit(O, cord[6])
                        tie += 1 

                if mouse_x >190 and mouse_x <343:
                    if board[2][1]=="X" or board[2][1]=="O":
                        print("This space is taken!")
                        count-=1

                    elif turn == True:
                        board[2][1]="X"
                        screen.blit(X, cord[7])
                        tie += 1 
                    else:
                        board[2][1]="O"
                        screen.blit(O, cord[7])
                        tie += 1 

                if mouse_x >343 and mouse_x <500:
                    if board[2][2]=="X" or board[2][2]=="O":
                        print("This space is taken!")
                        count-=1
                    elif turn == True:
                        board[2][2]="X"
                        screen.blit(X, cord[8])
                        tie += 1 
                    else:
                        board[2][2]="O"
                        screen.blit(O, (cord[8]))
                        tie += 1 





    draw_screen()
    draw_moves()

    if get_winner(board)==('X') or get_winner(board)==('O'):
         draw_text((get_winner(board)) + " Wins!", font, screen, 0, -0)

         turn=2
         
    elif tie == 9:
        draw_text(" It's a tie.", font, screen, 0, -0)
        



    main_clock.tick(60)



    if turn == True:
        draw_text('Player X. Choose.', font, screen, 450, 0)

    if turn == False:
        draw_text('Player O. Choose.', font, screen, 450,0)

    else:
        draw_text('', font, screen, 450,0)


    if count%2==0:
        turn=True
    else:
        turn=False

    pygame.display.update()


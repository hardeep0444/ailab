import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1

game = running
mark = 'X'

def DrawBoard():
  print(" %c | %c | %c " %(board[1],board[2],board[3]))
  print("___|___|___")
  print(" %c | %c | %c " %(board[4],board[5],board[6]))
  print("___|___|___")
  print(" %c | %c | %c " %(board[7],board[8],board[9]))
  print("   |   |   ")

def checkPosition(x):
  if (board[x]==' '):
    return True
  else:
    return False

def checkwin():
  global game

  if (board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
    game=win
  elif (board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
    game=win
  elif (board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
    game=win
  
  elif (board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
    game=win
  elif (board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
    game=win
  elif (board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
    game=win
  elif (board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
    game=win
  elif (board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
    game=win
  
  elif (board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
    game = draw
  
  else:
    game = running

print("Tic tac toe game")
print("Player 1 [X] -- Player 2 [O]")
print()
print()
print("Please wait.....")
time.sleep(3)

while(game==running):
  os.system('cls')
  DrawBoard()
  if (player%2==1):
    print("Player 1's chance")
    mark = 'X'
  else:
    print("Player 2's chance")
    mark = 'O'
  
  choice = int(input("Enter the position [1-9]"))
  if (checkPosition(choice)):
    board[choice]=mark
    player+=1
    checkwin()

os.system('cls')
DrawBoard()

if (game==draw):
  print("Game Draw")
elif (game==win):
  player-=1
  if (player%2!=0):
    print("player 1 won")
  else:
    print("Player 2 won")

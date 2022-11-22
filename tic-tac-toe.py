import random


def displayBoard(board):

  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')


def playerChoice():
  choice = ''
  while not (choice == 'X' or choice == 'O'):
    print('Do you want to be X or O?')
    choice = input().upper()
  
  if choice == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']



def firstPlayer():
  if random.randint(0, 1) == 0:
    return 'Vennela'
  else:
    return 'player'


def playAgain():
  print('Do you want to play again? : Yes or No')
  return input().lower().startswith('y')



def playerTurn(board, letter, move):
  board[move] = letter


def success(x, y):
  return ((x[7] == y and x[8] == y and x[9] == y) or 
        (x[4] == y and x[5] == y and x[6] == y) or 
        (x[1] == y and x[2] == y and x[3] == y) or 
        (x[7] == y and x[4] == y and x[1] == y) or 
        (x[8] == y and x[5] == y and x[2] == y) or 
        (x[9] == y and x[6] == y and x[3] == y) or 
        (x[7] == y and x[5] == y and x[3] == y) or 
        (x[9] == y and x[5] == y and x[1] == y)) 



def getBoard(board):
  copyBoard = []
  for i in board:
    copyBoard.append(i)
  return copyBoard

def freeSpace(board, move):
  return board[move] == ' '

def playerMove(board):
  move = ' '
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
    print('Where do you want to mark? :1-9 ')
    move = input()
  return int(move)

def randAvai(board, movesList):
  moves = []
  for i in movesList:
    if freeSpace(board, i):
      moves.append(i)
  
  if len(moves) != 0:
    return random.choice(moves)
  else:
    return None

def myMove(board, vennelaChoice):
  if vennelaChoice == 'X':
    playerLetter = 'O'
  else:
    playerLetter = 'X'

  for i in range(1, 10):
    copy = getBoard(board)
    if freeSpace(copy, i):
      playerTurn(copy, vennelaChoice, i)
      if success(copy, vennelaChoice):
        return i
  
  for i in range(1, 10):
    copy = getBoard(board)
    if freeSpace(copy, i):
      playerTurn(copy, playerLetter, i)
      if success(copy, playerLetter):
        return i
  move = randAvai(board, [1, 3, 7, 9])
  if move != None:
    return move

  if freeSpace(board, 5):
    return 5

  return randAvai(board, [2, 4, 6, 8])


def fullBoard(board):
  for i in range(1, 10):
    if freeSpace(board, i):
      return False
  return True


print('Welcome to Tic Tac Toe :)')

while True:
  board = [' '] * 10
  playerLetter, vennelaChoice = playerChoice()
  turn = firstPlayer()
  print('The ' + turn + ' will go first.')
  gameIsPlaying = True

  while gameIsPlaying:
    if turn == 'player':
      displayBoard(board)
      move = playerMove(board)
      playerTurn(board, playerLetter, move)
      if success(board, playerLetter):
        displayBoard(board)
        print('You have won the game!')
        gameIsPlaying = False
      else:
        if fullBoard(board):
          displayBoard(board)
          print('The game is a tie')
          break
        else:
          turn = 'Vennela'
    else:
      move = myMove(board, vennelaChoice)
      playerTurn(board, vennelaChoice, move)
      if success(board, vennelaChoice):
        displayBoard(board)
        print('Vennela has won.')
        gameIsPlaying = False
      else:
        if fullBoard(board):
         displayBoard(board)
         print('The game is a tie')
         break
        else:
          turn = 'player'

  if not playAgain():
    break
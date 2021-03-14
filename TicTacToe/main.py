import random
# from playsound import playsound
from os import system as sys

# Begin Game

# Random choice of starting player

# Display game board

win = True

gameWin = False
gameBoard = [' ', ' ', ' ',
				' ', ' ', ' ',
				' ', ' ', ' ']

def playerLoc(var1):
	if(var1 == "top left"):
		moveIdx = 0
	if (var1 == "top center"):
		moveIdx = 1
	if (var1 == "top right"):
		moveIdx = 2
	if (var1 == "middle left"):
		moveIdx = 3
	if (var1 == "middle" or var1 == "center"):
		moveIdx = 4
	if (var1 == "middle right"):
		moveIdx = 5
	if (var1 == "bottom left"):
		moveIdx = 6
	if (var1 == "bottom middle" or var1 == "bottom center"):
		moveIdx = 7
	if (var1 == "bottom right"):
		moveIdx = 8

	return moveIdx

def didGameEnd(moveChar):
  # if moveChar == 'xxx' or 'ooo':

	
  # Check board conditions (ex. check if top row all equal 'X' or 'O' aka the moveChar)
	if(gameBoard[0] == moveChar and gameBoard[1] == moveChar and      gameBoard[2] == moveChar):
		# The top row has all of the same X or O, so return true
	  return True
	if (gameBoard[3] == moveChar and gameBoard[4] == moveChar and     gameBoard[5] == moveChar):
		return True
	if (gameBoard[6] == moveChar and gameBoard[7] == moveChar and gameBoard[8] == moveChar):
		return True
	if (gameBoard[0] == moveChar and gameBoard[4] == moveChar and gameBoard[8] == moveChar):
		return True
	if (gameBoard[2] == moveChar and gameBoard[4] == moveChar and gameBoard[6] == moveChar):
		return True
	if (gameBoard[0] == moveChar and gameBoard[3] == moveChar and gameBoard[6] == moveChar):
		return True
	if (gameBoard[1] == moveChar and gameBoard[4] == moveChar and gameBoard[7] == moveChar):
		return True
	if (gameBoard[2] == moveChar and gameBoard[5] == moveChar and gameBoard[8] == moveChar):
		return True

	return False


# Check for Tie Game
def tieGame():
	for i in range(len(gameBoard)):
		# gameBoard(0-8) == moveChar
		if gameBoard[i]  == ' ':
			return False

	return True
			

  # if gameBoard[0,1,2,3,4,5,6,7,8] == moveChar:
	# 	print ("TIE GAME")  
	# 	return True
	

  

  

def displayBoard(board):
	print(" " + board[0] + " | " + board[1] + " | " + board[2])
	print("---+---+---")
	print(" " + board[3] + " | " + board[4] + " | " + board[5])
	print("---+---+---")
	print(" " + board[6] + " | " + board[7] + " | " + board[8])

def makeMove(loc, moveChar):
  gameBoard[loc] = moveChar

def gameStart():
	global gameWin
	# Pick first player
	playerFirst = random.randint(1,2)
	
	# Print setup?

	# Loop game
	while not gameWin:
		displayBoard(gameBoard)

		if playerFirst == 1:
			move1 = input("WHERE WOULD YOU LIKE TO MOVE?  ")
			move1 = playerLoc(move1)
			makeMove(move1, 'X')
			# Check for game win / tie
			if(didGameEnd('X')):
				sys("clear")
				displayBoard(gameBoard)
				print("PLAYER 1 WON THE GAME! PLAYER 2 HAS LOST.")
				gameWin = True
			elif(tieGame()):
				print("-- TIE GAME, NO ONE WINS. -- ")
				gameWin = True
			if(not gameWin):
				print ("                                                                       ---NEXT TURN---\n         ")
				sys("clear")
			playerFirst = 2
		else:
			move2 = input("WHERE WOULD YOU LIKE TO MOVE?  ")
			move2 = playerLoc(move2)
			makeMove(move2, 'O')
			# Check for game win / tie
			if(didGameEnd('O')):
				sys("clear")
				displayBoard(gameBoard)
				print("PLAYER 2 WON THE GAME! PLAYER 1 HAS LOST.")
				gameWin = True
			elif(tieGame()):
				print("-- TIE GAME, NO ONE WINS. -- ")
				gameWin = True
			if(not gameWin):
				print ("                                                                       ---NEXT TURN---\n         ")
				sys("clear")
			playerFirst = 1
      
    
def initiate():
	# playsound('Friendly-Machines_Looping.mp3')

	# Print title screen
  # Try using Turtle to illustrate the words "Tic Tac Toe" in big letters
	print("TIC TAC TOE\n")
	input("TO START 2 PLAYER MODE PRESS ENTER\n")

	sys("clear")
	
	# Print instructions
	print("YOU NEED 2 PLAYERS TO PLAY THE GAME,")
	print("AND ONE PERSON GOES AT A TIME.")
	print("TO WIN THE GAME YOU MUST HAVE A ROW OF X'S OR O'S,")
	print("AND THE FIRST PERSON TO START PLAYING WILL USE X.")
	print("THE SECOND PERSON WILL USE O.")
	print("REMEMBER, YOU CAN'T USE A SPACE THAT IS ALREADY TAKEN,")
	print("YOU MUST USE A NEW SPOT EVERY TIME.")
	print("THE GAME IS PLAYED ON A 3X3 BOARD.")
	print("HAVE FUN PLAYING!\n")
	input("CLICK ENTER TO CONTINUE  ")
	sys("clear")
    
	# Start game
	gameStart()

	# newGame = input("WOULD YOU LIKE TO PLAY TIC TAC TOE AGAIN?  ")

	# if newGame == "yes" or newGame == "Yes":
	# 	initiate()





initiate() 

# Keystrokes
'''
r = readchar.readkey()#get the key input
if r == 'a':
	print("A was pressed")
'''
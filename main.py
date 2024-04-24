#SAÑO, JAMIE JASMINE
# BSCS 3B
# MACHINE PROBLEM 4
from AlphaBeta import *
from Board import *
from Heuristics import *
import time

alpha = float('-inf')
beta = float('inf')
depth = 3
ai_depth = 4

def boardOutput(board):
		
		print(board[0]+"(00)----------------------"+board[1]+"(01)----------------------"+board[2]+"(02)");
		print("|                           |                           |");
		print("|       "+board[8]+"(08)--------------"+board[9]+"(09)--------------"+board[10]+"(10)     |");
		print("|       |                                        |      |");
		print(board[3]+"(03)---"+board[11]+"(11)                                 "+board[12]+"(12)---"+board[4]+"(04)");
		print("|       |                                        |      |");
		print("|       "+board[13]+"(13)--------------"+board[14]+"(14)--------------"+board[15]+"(15)     |");
		print("|                           |                           |");
		print(board[5]+"(05)----------------------"+board[6]+"(06)----------------------"+board[7]+"(07)\n\n");



def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):
	
	board = []
	for i in range(16):
		board.append("X")

	evaluation = checker()
		
	for i in range(6):

		boardOutput(board)
		finished = False
		while not finished:
			try:
                
				pos = int(input("++ INPUT ++\nPlace '1' piece (**): "))	
				
				if board[pos] == "X":
					board[pos] = '1'
					if isCloseMill(pos, board):
						itemPlaced = False
						while not itemPlaced:
							try:
								pos = int(input("\nRemove '2' piece (): "))
								if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNoPieces(board, "1") == 3):
									board[pos] = "X"
									itemPlaced = True
								else:
									print("\nOops! Invalid position.")
							except Exception:
								print("\n Oh no! Input was either out of bounds or wasn't an integer.")
					finished = True
				else:
					print("\nUh-oh! There is already a piece there.")
			except Exception:
				print("\n Sorry, couldn't get the input value.")
		
		boardOutput(board)
		evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True, heuristic_stage1)

		if evalBoard.checker == float('-inf'):
			print("\n\n __   __     _     ___   _____  ___")
			print("|  | |  |   | |   |   | |  |__ | -_|")
			print("|  |_|  |   | |__ | | | |___  || |_")
			print("|_______|   |____||___|  ___|_||___|")
			exit(0)
		else:
			board = evalBoard.board

	endStagesFinished = False
	while not endStagesFinished:

		boardOutput(board)
		
		userHasMoved = False
		while not userHasMoved:
			try:
				pos = int(input("\nMove '1' piece: "))
				while board[pos] != '1':
					pos = int(input("\nMove '1' piece: ")) 
				userHasPlaced = False
				while not userHasPlaced:
					newPos = int(input("'1' New Location: "))
					if board[newPos] == "X":
						board[pos] = 'X'
						board[newPos] = '1'
						if isCloseMill(newPos, board):
							userHasRemoved = False
							while not userHasRemoved:
								try:
									pos = int(input("\nRemove '2' piece: "))
									
									if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNoPieces(board, "1") == 3):
										board[pos] = "X"
										userHasRemoved = True
									else:
										print("\nOops! Invalid position.")
								except Exception:
									print("\nError! While accepting input")
						userHasPlaced = True
						userHasMoved = True
					else:
						print("\nUh-oh! There is already a piece there.")

			except Exception:
				print("\n Sorry, you can't move here.")

		if getEvaluationStage23(board) == float('inf'):
			print("\n\n __   __    _      _  ___  __")
			print("|  | |  |  | | __ | ||   ||  |____")
			print("|  |_|  |  | |_||_| || | ||  ___  |")
			print("|_______|  |________||___||__| |__|")
			exit(0)

		boardOutput(board)

		evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False, heuristic_stage23)

		if evaluation.checker == float('-inf'):
			print("\n\n __   __     _     ___   _____  ___")
			print("|  | |  |   | |   |   | |  |__ | -_|")
			print("|  |_|  |   | |__ | | | |___  || |_")
			print("|_______|   |____||___|  ___|_||___|")
			exit(0)
		else:
			board = evaluation.board


if __name__ == "__main__":	
    print("============================================================================================================")
    print("||   ______                                __                                                              ||")
    print("||  |   ___|    _________   ___   __      |__|                                                             ||")
    print("||  |  |___    |  _   _  | |   | |  |____      ________      _________                          ________   ||")
    print("||  |  __  |   | | | | | | | __| |  ___  |    |    ____|    |  _   _  | ______  _     _     _  |    ____|  ||")
    print("||  | |__| |   | | |_| | | | |_  |  | |  |    |   |____     | | | | | ||      || |__ | |__ | | |   |____   ||")
    print("||  |______|   |_|     |_| |___| |__| |__|    |____    |    | | |_| | ||      ||  __||  __|| | |____    |  ||") 
    print("||                                             ____|   |    |_|     |_||______||_|   |_|   |_|  ____|   |  ||") 
    print("||                                            |________|                                       |________|  ||")
    print("============================================================================================================")
	
    print("= Submitted By: Jamie Jasmine Saño        BSCS - 3B                       Machine Problem 4 - Human VS AI =\n\n")
	
    print("++  BOARD  ++")
    HUMAN_VS_AI(numberOfPiecesHeuristic, AdvancedHeuristic)
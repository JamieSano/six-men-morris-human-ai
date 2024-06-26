#SAÑO, JAMIE JASMINE
# BSCS 3B
# MACHINE PROBLEM 4
from Utility import *
import copy

def adjacentLocations(position):
	adjacent = [
		[1, 3],
		[0, 2, 9],
		[1, 4],
		[0, 5, 11],
		[2, 7, 12],
		[3, 6],
		[5, 7, 14],
		[4, 6],
		[9, 11],
		[1, 8, 10],
		[9, 12],
		[3, 8, 13],
		[4, 10, 15],
		[11, 14],
		[6, 13, 15],
		[12, 14]
	]
	return adjacent[position]

def checkMillFormation(position, board, player):
	mill = [
			(isMill(player, board, 1, 2) or isMill(player, board, 3, 5)),
			(isMill(player, board, 0, 2) or isMill(player, board, 9, 1)),
			(isMill(player, board, 0, 1) or isMill(player, board, 4, 7)),
			(isMill(player, board, 0, 5) or isMill(player, board, 11, 13)),
			(isMill(player, board, 2, 7) or isMill(player, board, 12, 10)),
			(isMill(player, board, 0, 3) or isMill(player, board, 6, 7)),
			(isMill(player, board, 5, 7) or isMill(player, board, 14, 15)),
			(isMill(player, board, 2, 4) or isMill(player, board, 5, 6)),
			(isMill(player, board, 9, 10) or isMill(player, board, 11, 13)),
			(isMill(player, board, 1, 8) or isMill(player, board, 10, 15)),
			(isMill(player, board, 8, 9) or isMill(player, board, 12, 15)),
			(isMill(player, board, 0, 3) or isMill(player, board, 8, 13)),
			(isMill(player, board, 4, 12) or isMill(player, board, 10, 15)),
			(isMill(player, board, 8, 11) or isMill(player, board, 14, 15)),
			(isMill(player, board, 6, 5) or isMill(player, board, 13, 15)),
			(isMill(player, board, 10, 12) or isMill(player, board, 13, 14))
	]
	return mill[position]

def isMill(player, board, pos1, pos2):
	if (board[pos1] == player and board[pos2] == player):
		return True
	return False

def isCloseMill(position, board):
	player = board[position]

	# if position is not empty
	if (player != "X"):
		return checkMillFormation(position, board, player)
	
	return False

def stage1Moves(board):
	board_list = []

	for i in range(len(board)):
		# fill empty positions with white
		if (board[i] == "X"):
			board_clone = copy.deepcopy(board)
			board_clone[i] = "1"

			if (isCloseMill(i, board_clone)):
				board_list = removePiece(board_clone, board_list)
			else:
				board_list.append(board_clone)
	return board_list

def stage2Moves(board):
	board_list = []
	for i in range(len(board)):
		if (board[i] == "1"):
			adjacent_list = adjacentLocations(i)

			for pos in adjacent_list:
				if (board[pos] == "X"):
					board_clone = copy.deepcopy(board)
					board_clone[i] = "X"
					board_clone[pos] = "1"

					if isCloseMill(pos, board_clone):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

def stage3Moves(board):
	board_list = []

	for i in range(len(board)):
		if (board[i] == "1"):

			for j in range(len(board)):
				if (board[j] == "X"):
					board_clone = copy.deepcopy(board)

					board_clone[i] = "X"
					board_clone[j] = "1"

					if (isCloseMill(j, board_clone)):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

def stage23Moves(board):
	if (numValue(board, "1") == 3):
		return stage3Moves(board)
	else:
		return stage2Moves(board)

def removePiece(board_clone, board_list):
	'''
	'''
	for i in range(len(board_clone)):
		if (board_clone[i] == "2"):

			if not isCloseMill(i, board_clone):
				new_board = copy.deepcopy(board_clone)
				new_board[i] = "X"
				board_list.append(new_board)
	return board_list

def getPossibleMillCount(board, player):
	count = 0

	for i in range(len(board)):
		if (board[i] == "X"):
			if checkMillFormation(i, board, player):
				count += 1
	return count

def getEvaluationStage23(board):
	numWhitePieces = numValue(board, "1")
	numBlackPieces = numValue(board, "2")
	mills = getPossibleMillCount(board, "1")

	evaluation = 0

	board_list = stage23Moves(board)

	numBlackMoves = len(board_list)

	if numBlackPieces <= 2 or numBlackPieces == 0:
		return float('inf')
	elif numWhitePieces <= 2:
		return float('-inf')
	else:
		return 0

def potentialMillInFormation(position, board, player):
	adjacent_list = adjacentLocations(position)

	for i in adjacent_list:
		if (board[i] == player) and (not checkMillFormation(position, board, player)):
			return True
	return False

def getPiecesInPotentialMillFormation(board, player):
	count = 0
	for i in range(len(board)):
		if (board[i] == player):
			adjacent_list = adjacentLocations(i)
			for pos in adjacent_list:
				if (player == "1"):
					if (board[pos] == "2"):
						board[i] = "2"
						if isCloseMill(i, board):
							count += 1
						board[i] = player
				else:
					if (board[pos] == "1" and potentialMillInFormation(pos, board, "1")):
						count += 1
	return count
#SAÑO, JAMIE JASMINE
# BSCS 3B
# MACHINE PROBLEM 4
from Board import *

def numberOfPiecesHeuristic(board, isStage1):
	numPlayerOneTokens = numValue(board, "1")
	numPlayerTwoTokens = numValue(board, "2")

	moveablePiecesPlayer2 = 0

	if not isStage1:
		movablePiecesBlack = len(stage23Moves(board))

	if not isStage1:
		if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numPlayerOneTokens <= 2:
			evaluation = float('-inf')
		else:
			evaluation = 200 * (numPlayerOneTokens - numPlayerTwoTokens)
	else:
		evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)

	return evaluation

def potentialMillsHeuristic(board, isStage1):
	evaluation = 0

	numPlayerOneTokens = numValue(board, "1")
	numPlayerTwoTokens = numValue(board, "2")

	numPossibleMillsPlayer1 = getPossibleMillCount(board, "1")
	numPossibleMillsPlayer2 = getPossibleMillCount(board, "2")

	moveablePiecesPlayer2 = 0

	if not isStage1:
		movablePiecesBlack = len(stage23Moves(board))

	potentialMillsPlayer1 = getPiecesInPotentialMillFormation(board, "1")
	potentialMillsPlayer2 = getPiecesInPotentialMillFormation(board, "2")

	if not isStage1:
		if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numPlayerOneTokens <= 2:
			evaluation = float('-inf')
		else:
			if (numPlayerOneTokens < 4):
				evaluation += 100 * numPossibleMillsPlayer1
				evaluation += 200 * potentialMillsPlayer2
			else:
				evaluation += 200 * numPossibleMillsPlayer1
				evaluation += 100 * potentialMillsPlayer2
	else:
		if numPlayerOneTokens < 4:
			evaluation += 100 * numPossibleMillsPlayer1
			evaluation += 200 * potentialMillsPlayer2
		else:
			evaluation += 200 * numPossibleMillsPlayer1
			evaluation += 100 * potentialMillsPlayer2

	return evaluation

def numberOfMoveablePiecesHeuristic(board, isStage1):
	evaluation = 0

	numPlayerOneTokens = numValue(board, "1")
	numPlayerTwoTokens = numValue(board, "2")

	moveablePiecesPlayer1 = 0
	moveablePiecesPlayer2 = 0

	if not isStage1:
		movablePiecesBlack = len(stage23Moves(board))

	if not isStage1:
		if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numPlayerOneTokens <= 2:
			evaluation = float('-inf')
		else:
			evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)
			evaluation -= 50 * movablePiecesBlack
	else:
		evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)
		evaluation -= 50 * moveablePiecesPlayer2

	return evaluation


def AdvancedHeuristic(board, isStage1):
	evaluation = 0

	numPlayerOneTokens = numValue(board, "1")
	numPlayerTwoTokens = numValue(board, "2")

	numPossibleMillsPlayer1 = getPossibleMillCount(board, "1")
	numPossibleMillsPlayer2 = getPossibleMillCount(board, "2")

	moveablePiecesPlayer1 = 0
	moveablePiecesPlayer2 = 0

	if not isStage1:
		movablePiecesBlack = len(stage23Moves(board))

	potentialMillsPlayer1 = getPiecesInPotentialMillFormation(board, "1")
	potentialMillsPlayer2 = getPiecesInPotentialMillFormation(board, "2")

	if not isStage1:
		if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numPlayerOneTokens <= 2:
			evaluation = float('-inf')
		else:
			if (numPlayerOneTokens < 4):
				evaluation += 100 * numPossibleMillsPlayer1
				evaluation += 200 * potentialMillsPlayer2
			else:
				evaluation += 200 * numPossibleMillsPlayer1
				evaluation += 100 * potentialMillsPlayer2
			evaluation -= 25 * movablePiecesBlack
			evaluation += 50 * (numPlayerOneTokens - numPlayerTwoTokens)
	else:
		if numPlayerOneTokens < 4:
			evaluation += 100 * numPossibleMillsPlayer1
			evaluation += 200 * potentialMillsPlayer2
		else:
			evaluation += 200 * numPossibleMillsPlayer1
			evaluation += 100 * potentialMillsPlayer2
		evaluation -= 25 * moveablePiecesPlayer2
		evaluation += 50 * (numPlayerOneTokens - numPlayerTwoTokens)

	return evaluation
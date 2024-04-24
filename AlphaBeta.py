#SAÑO, JAMIE JASMINE
# BSCS 3B
# MACHINE PROBLEM 4
from Board import *
from Utility import *

pruned = 0
visited_states = 0
class checker():
    def __init__(self):
        self.checker = 0
        self.board = []

def alphaBetaPruning(board, depth, human, alpha, beta, isStage1, heuristic):
    finalChecking = checker()
    global visited_states
    visited_states += 1

    if depth != 0:
        currentChecking = checker()
        if human:
            if isStage1:
                possible_config = stage1Moves(board)
            else:
                possible_config = stage23Moves(board)
        else:
            if isStage1:
                possible_config = generateInvertedBoardList(stage1Moves(InvertedBoard(board)))
            else:
                possible_config = generateInvertedBoardList(stage23Moves(InvertedBoard(board)))
    
        for move in possible_config:
            if human:
                currentChecking = alphaBetaPruning(move, depth - 1, False, alpha, beta, isStage1, heuristic)
                if currentChecking.checker > alpha:
                    alpha = currentChecking.checker
                    finalChecking.board = move
            else:
                currentChecking = alphaBetaPruning(move, depth - 1, True, alpha, beta, isStage1, heuristic)

                if currentChecking.checker < beta:
                    beta = currentChecking.checker
                    finalChecking.board = move
            
            if alpha >= beta:
                global pruned
                pruned += 1
                break
        if human:
            finalChecking.checker = alpha
        else:
            finalChecking.checker = beta
    else:
        if human:
            finalChecking.checker = heuristic(board, isStage1)
        else:
            finalChecking.checker = heuristic(InvertedBoard(board), isStage1)
    return finalChecking

def getPruned():
	global pruned
	x = pruned
	pruned = 0
	return x

def getStatesVisited():
	global visited_states
	x = visited_states
	visited_states = 0
	return x
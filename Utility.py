#SAÑO, JAMIE JASMINE
# BSCS 3B
# MACHINE PROBLEM 4
import copy

def numValue(board, value):
    return board.count(value)

def InvertedBoard(board):
    i_board = []
    for i in board:
        if i == "1":
            i_board.append("2")
        elif i == "2":
            i_board.append("1")
        else:
            i_board.append("X")
    return i_board

def generateInvertedBoardList(position_list):
    result = []
    for i in position_list:
        result.append(InvertedBoard(i))
    return result
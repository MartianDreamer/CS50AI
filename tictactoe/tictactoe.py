"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_empty = sum([row.count(EMPTY) for row in board])
    # if count empty is odd X can play else O can play
    return X if count_empty % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avail_actions = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] is EMPTY:
                avail_actions.append((row, col))
    return avail_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] > 3 or action[1] < 0 or action[1] > 3 or board[action[0]][action[1]] is not EMPTY:
        raise ValueError("invalid action")
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0,3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(0,3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[1][1] == board[2][2] == board[3][3] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

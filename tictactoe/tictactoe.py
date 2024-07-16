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
    avail_actions = set()
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] is EMPTY:
                avail_actions.add((row, col))
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
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return True
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    count_empty = sum([row.count(EMPTY) for row in board])
    return count_empty == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    return 1 if the_winner == X else -1 if the_winner == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    selected_player = player(board)
    available_actions = actions(board)
    optimal_move = (None, None)
    if selected_player == X:
        for action in available_actions:
            new_board = result(board, action)
            value = min_minimax(new_board, optimal_move[0])
            if optimal_move[0] is None or value > optimal_move[0]:
                optimal_move = (value, action)
        return optimal_move[1]
    else:
        for action in available_actions:
            new_board = result(board, action)
            value = max_minimax(new_board, optimal_move[0])
            if optimal_move[0] is None or value < optimal_move[0]:
                optimal_move = (value, action)
        return optimal_move[1]


def min_minimax(board, lower_bound=None):
    """
    Return point for a board as min player
    """
    if terminal(board):
        return utility(board)
    available_actions = actions(board)
    current_min = 1
    for action in available_actions:
        new_board = result(board, action)
        value = max_minimax(new_board)
        if lower_bound is not None and value < lower_bound:
            return value
        current_min = min(current_min, value)
    return current_min


def max_minimax(board, upper_bound=None):
    """
    Return point for a board as max player
    """
    if terminal(board):
        return utility(board)
    available_actions = actions(board)
    current_max = -1
    for action in available_actions:
        new_board = result(board, action)
        value = min_minimax(new_board)
        if upper_bound is not None and value > upper_bound:
            return value
        current_max = max(current_max, value)
    return current_max

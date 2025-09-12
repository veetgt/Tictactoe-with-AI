import math
import copy

X = "X"
O = "O"
EMPTY = None

# --- Starting state ---
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Who has the next turn on a board
def player(board):
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    if countX > countO:
        return O
    else:
        return X

def actions(board):
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    board_backup = board
    if action not in actions(board):
        raise ValueError("Invalid action")
    updated_board = copy.deepcopy(board)
    player_move = player(board)

    i, j = action
    updated_board[i][j] = player_move

    return updated_board

def winner(board):
    # Check winner

    # Horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
    
    # Vertical
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
        
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2] 
    
    # If no one wins
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    if not actions(board):
        return True
    return False

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_move = action
            return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_move = action
        return best_move
        
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v
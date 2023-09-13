import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x = 0
    o = 0
    for fila in board:
        for elemento in fila:
            if elemento == X:
                x += 1
            elif elemento == O:
                o += 1
    if x == o:
        return X
    else:
        return O


def actions(board):
    acciones = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acciones.append((i, j))
    return acciones


def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    else:
        i,j = action
        resultado = []
        for fila in board:
            r = []
            for elemento in fila:
                r.append(elemento)
            resultado.append(r)
        resultado[i][j] = player(board)
    return resultado


def winner(board):
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    elif board[1][1] == board[0][1] == board[2][1] != EMPTY:
        return board[1][1]
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return board[i][0]
            elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
                return board[0][i]
        return None


def terminal(board):
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    elif board[1][1] == board[0][1] == board[2][1] != EMPTY:
        return True
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return True
            elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
                return True
        for fila in board:
            for elemento in fila:
                if elemento == EMPTY:
                    return False
        return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    def minimax_recursive(board):

        if terminal(board):
            return utility(board), None
        
        if player(board) == X:
            value = float("-inf") 
            best_move = None
            for action in actions(board):
                new_value, _ = minimax_recursive(result(board, action))
                if new_value > value:
                    value, best_move = new_value, action
            return value, best_move

        else:
            value = float("inf")
            best_move = None
            for action in actions(board):
                new_value, _ = minimax_recursive(result(board, action))
                if new_value < value:
                    value, best_move = new_value, action
            return value, best_move

    _, move = minimax_recursive(board)
    return move
def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_rook_moves(board, row, col):
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        for i in range(1, 8):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board[r][c]
                if target_piece == ' ':
                    moves.append((r, c))
                elif target_piece.islower() != board[row][col].islower():
                    moves.append((r, c))
                    break
                else:
                    break
            else:
                break
    return moves

def generate_knight_moves(board, row, col):
    moves = []
    possible_moves = [
        (row - 2, col - 1), (row - 2, col + 1),
        (row - 1, col - 2), (row - 1, col + 2),
        (row + 1, col - 2), (row + 1, col + 2),
        (row + 2, col - 1), (row + 2, col + 1),
    ]
    for r, c in possible_moves:
        if 0 <= r < 8 and 0 <= c < 8:
            target_piece = board[r][c]
            if target_piece == ' ' or target_piece.islower() != board[row][col].islower():
                moves.append((r, c))
    return moves

def generate_bishop_moves(board, row, col):
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        for i in range(1, 8):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board[r][c]
                if target_piece == ' ':
                    moves.append((r, c))
                elif target_piece.islower() != board[row][col].islower():
                    moves.append((r, c))
                    break
                else:
                    break
            else:
                break
    return moves

def generate_queen_moves(board, row, col):
    return generate_rook_moves(board, row, col) + generate_bishop_moves(board, row, col)

def generate_king_moves(board, row, col):
    moves = []
    possible_moves = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                 (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
    ]
    for r, c in possible_moves:
        if 0 <= r < 8 and 0 <= c < 8:
            target_piece = board[r][c]
            if target_piece == ' ' or target_piece.islower() != board[row][col].islower():
                moves.append((r, c))
    return moves

def generate_pawn_moves(board, row, col):
    moves = []
    piece = board[row][col]
    direction = -1 if piece.isupper() else 1
    start_row = 6 if piece.isupper() else 1
    if 0 <= row + direction < 8 and board[row+direction][col] == ' ':
        moves.append((row+direction, col))
        if row == start_row and board[row+2*direction][col] == ' ':
            moves.append((row+2*direction, col))
    if 0 <= row + direction < 8 and 0 <= col + 1 < 8 and board[row+direction][col+1].islower() != piece.islower() and board[row+direction][col+1] != ' ':
        moves.append((row+direction, col + 1))
    if 0 <= row + direction < 8 and 0 <= col - 1 < 8 and board[row+direction][col-1].islower() != piece.islower() and board[row+direction][col-1] != ' ':
        moves.append((row+direction, col - 1))
    return moves

def is_check(board, color):
    king_pos = None
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == ('K' if color == 'white' else 'k'):
                king_pos = (r, c)
                break
        if king_pos:
            break

    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != ' ' and piece.islower() != (color == 'white'):
                if piece.lower() == 'r':
                    possible_moves = generate_rook_moves(board, r, c)
                elif piece.lower() == 'n':
                    possible_moves = generate_knight_moves(board, r, c)
                elif piece.lower() == 'b':
                    possible_moves = generate_bishop_moves(board, r, c)
                elif piece.lower() == 'q':
                    possible_moves = generate_queen_moves(board, r, c)
                elif piece.lower() == 'k':
                    possible_moves = generate_king_moves(board, r, c)
                elif piece.lower() == 'p':
                    possible_moves = generate_pawn_moves(board, r, c)
                else:
                    possible_moves = []
                if king_pos in possible_moves:
                    return True
    return False

# Example usage (testing):
board = initialize_board()
print_board(board)

print("White in check?", is_check(board, 'white'))
print("Black in check?", is_check(board, 'black'))

board[0][0] = ' '
board[5][0] = 'r'
print_board(board)
print("White in check?", is_check(board, 'white')) #now white is in check

board[7][4] = ' '
board[2][4] = 'K'
print_board(board)
print("White in check?", is_check(board, 'white')) #now white is not in check

def get_legal_moves(board, color):

    legal_moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != ' ' and (piece.isupper() == (color == 'white')): #check if it is the correct color
                if piece.lower() == 'r':
                    possible_moves = generate_rook_moves(board, row, col)
                elif piece.lower() == 'n':
                    possible_moves = generate_knight_moves(board, row, col)
                elif piece.lower() == 'b':
                    possible_moves = generate_bishop_moves(board, row, col)
                elif piece.lower() == 'q':
                    possible_moves = generate_queen_moves(board, row, col)
                elif piece.lower() == 'k':
                    possible_moves = generate_king_moves(board, row, col)
                elif piece.lower() == 'p':
                    possible_moves = generate_pawn_moves(board, row, col)
                else:
                    possible_moves = []
                for move in possible_moves:
                    temp_board = [row[:] for row in board] #create a copy of the board
                    temp_board[move[0]][move[1]] = temp_board[row][col]
                    temp_board[row][col] = ' '
                    if not is_check(temp_board, color): #check if the move puts the king in check
                        legal_moves.append(((row, col), move))
    return legal_moves

def evaluate_board(board):
    score = 0
    piece_values = {'p': -1, 'r': -5, 'n': -3, 'b': -3, 'q': -9, 'k': -100,
                    'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, 'K': 100}
    for row in board:
        for piece in row:
            score += piece_values.get(piece, 0)
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_legal_moves(board, 'white'):
            temp_board = [row[:] for row in board]
            temp_board[move[1][0]][move[1][1]] = temp_board[move[0][0]][move[0][1]]
            temp_board[move[0][0]][move[0][1]] = ' '
            eval = minimax(temp_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)  # Update alpha
            if beta <= alpha:  # Beta cutoff
                break  # Prune the rest of the moves
        return max_eval
    else:  # Minimizing player (black)
        min_eval = float('inf')
        for move in get_legal_moves(board, 'black'):
            temp_board = [row[:] for row in board]
            temp_board[move[1][0]][move[1][1]] = temp_board[move[0][0]][move[0][1]]
            temp_board[move[0][0]][move[0][1]] = ' '
            eval = minimax(temp_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)  # Update beta
            if beta <= alpha:  # Alpha cutoff
                break  # Prune the rest of the moves
        return min_eval

def find_best_move(board, depth):
    best_move = None
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for move in get_legal_moves(board, 'white'):
        temp_board = [row[:] for row in board]
        temp_board[move[1][0]][move[1][1]] = temp_board[move[0][0]][move[0][1]]
        temp_board[move[0][0]][move[0][1]] = ' '
        eval = minimax(temp_board, depth - 1, alpha, beta, False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move
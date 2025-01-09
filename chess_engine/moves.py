from chess_engine.board import initialize_board

def generate_rook_moves(board, row, col):
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        for i in range(1, 8):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board[r][c]
                if target_piece == ' ':  # Empty square
                    moves.append((r, c))
                elif target_piece.islower() != board[row][col].islower():  # Capture opponent's piece
                    moves.append((r, c))
                    break  # Stop after capturing a piece
                else:
                    break  # Stop if hitting our own piece
            else:
                break  # Stop if going off the board
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
                    break  # Stop after capturing a piece
                else:
                    break  # Stop if hitting our own piece
            else:
                break  # Stop if going off the board
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
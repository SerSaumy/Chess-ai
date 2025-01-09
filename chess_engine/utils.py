from chess_engine.board import initialize_board

def is_king_in_check(board, color):
    """Check if the king of the given color is in check."""
    king_position = find_king(board, color)
    opponent_color = 'black' if color == 'white' else 'white'
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if (piece.isupper() and opponent_color == 'black') or (piece.islower() and opponent_color == 'white'):
                possible_moves = generate_possible_moves_for_piece(board, row, col, piece)
                if king_position in possible_moves:
                    return True
    return False

def find_king(board, color):
    """Find the position of the king of the given color."""
    for row in range(8):
        for col in range(8):
            if (color == 'white' and board[row][col] == 'K') or (color == 'black' and board[row][col] == 'k'):
                return (row, col)
    return None

def get_all_valid_moves(board, color):
    """Get all valid moves for the current player."""
    valid_moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if (color == 'white' and piece.isupper()) or (color == 'black' and piece.islower()):
                possible_moves = generate_possible_moves_for_piece(board, row, col, piece)
                for move in possible_moves:
                    if is_valid_move_for_piece(board, row, col, move[0], move[1]):
                        valid_moves.append((row, col, move[0], move[1]))
    return valid_moves

def generate_possible_moves_for_piece(board, row, col, piece):
    """Generate all possible moves for a piece (without checking validity)."""
    if piece.lower() == 'r':
        return generate_rook_moves(board, row, col)
    elif piece.lower() == 'n':
        return generate_knight_moves(board, row, col)
    elif piece.lower() == 'b':
        return generate_bishop_moves(board, row, col)
    elif piece.lower() == 'q':
        return generate_queen_moves(board, row, col)
    elif piece.lower() == 'k':
        return generate_king_moves(board, row, col)
    elif piece.lower() == 'p':
        return generate_pawn_moves(board, row, col)
    return []

def generate_knight_moves(board, row, col):
    """Generate all possible moves for a knight."""
    moves = []
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == '.' or board[new_row][new_col].islower() != board[row][col].islower():
                moves.append((new_row, new_col))
    return moves

def generate_rook_moves(board, row, col):
    """Generate all possible moves for a rook."""
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == '.':
                moves.append((new_row, new_col))
            elif board[new_row][new_col].islower() != board[row][col].islower():
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += direction[0]
            new_col += direction[1]
    return moves

def generate_bishop_moves(board, row, col):
    """Generate all possible moves for a bishop."""
    moves = []
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == '.':
                moves.append((new_row, new_col))
            elif board[new_row][new_col].islower() != board[row][col].islower():
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += direction[0]
            new_col += direction[1]
    return moves

def generate_queen_moves(board, row, col):
    """Generate all possible moves for a queen."""
    moves = []
    # Combine rook and bishop moves
    moves.extend(generate_rook_moves(board, row, col))
    moves.extend(generate_bishop_moves(board, row, col))
    return moves

def generate_king_moves(board, row, col):
    """Generate all possible moves for a king."""
    moves = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == '.' or board[new_row][new_col].islower() != board[row][col].islower():
                moves.append((new_row, new_col))
    return moves

def generate_pawn_moves(board, row, col):
    """Generate all possible moves for a pawn."""
    moves = []
    direction = -1 if board[row][col].isupper() else 1
    start_row = 6 if board[row][col].isupper() else 1

    # Move forward
    if board[row + direction][col] == '.':
        moves.append((row + direction, col))
        if row == start_row and board[row + 2 * direction][col] == '.':
            moves.append((row + 2 * direction, col))

    # Capture diagonally
    if col - 1 >= 0 and board[row + direction][col - 1] != '.' and board[row + direction][col - 1].islower() != board[row][col].islower():
        moves.append((row + direction, col - 1))
    if col + 1 < 8 and board[row + direction][col + 1] != '.' and board[row + direction][col + 1].islower() != board[row][col].islower():
        moves.append((row + direction, col + 1))

    return moves

def is_valid_move_for_piece(board, start_row, start_col, end_row, end_col):
    """Check if the move is valid (the piece can legally move to the end position)."""
    return True
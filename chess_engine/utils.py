from .moves import generate_rook_moves, generate_knight_moves, generate_bishop_moves, generate_queen_moves, generate_king_moves, generate_pawn_moves
def is_king_in_check(board, color):
    """Check if the king of the given color is in check."""
    king_position = find_king(board, color)
    opponent_color = 'black' if color == 'white' else 'white'
    
    # Check if any opponent piece can attack the king
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if (piece.isupper() and opponent_color == 'black') or (piece.islower() and opponent_color == 'white'):
                possible_moves = generate_possible_moves_for_piece(board, row, col, piece)
                if king_position in possible_moves:
                    return True  # King is in check
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

def is_valid_move_for_piece(board, start_row, start_col, end_row, end_col):
    """Check if the move is valid (the piece can legally move to the end position)."""
    # Here you would need to check if the piece can move to the end position based on its type and the board state.
    # For simplicity, this could just check for basic legality without castling, en passant, etc.
    return True

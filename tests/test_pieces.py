import pytest
from chess_engine.pieces import King, Queen, Rook, Knight, Bishop, Pawn
from chess_engine.board import initialize_board

def test_king_moves():
    """Test that the King moves correctly."""
    king = King('white')
    board = initialize_board()
    moves = king.possible_moves(board, 0, 4)  # King's position is e1 (row 0, col 4)
    assert (1, 4) in moves  # King should be able to move one square down

def test_queen_moves():
    """Test that the Queen moves correctly."""
    queen = Queen('black')
    board = initialize_board()
    moves = queen.possible_moves(board, 0, 3)  # Queen's position is d1 (row 0, col 3)
    assert (1, 3) in moves  # Queen can move one square down

def test_rook_moves():
    """Test that the Rook moves correctly."""
    rook = Rook('white')
    board = initialize_board()
    moves = rook.possible_moves(board, 0, 0)  # Rook's position is a1 (row 0, col 0)
    assert (1, 0) in moves  # Rook can move one square down

def test_knight_moves():
    """Test that the Knight moves correctly."""
    knight = Knight('black')
    board = initialize_board()
    moves = knight.possible_moves(board, 7, 1)  # Knight's position is b8 (row 7, col 1)
    assert (5, 2) in moves  # Knight can move to (5, 2)

def test_bishop_moves():
    """Test that the Bishop moves correctly."""
    bishop = Bishop('white')
    board = initialize_board()
    moves = bishop.possible_moves(board, 0, 2)  # Bishop's position is c1 (row 0, col 2)
    assert (1, 3) in moves  # Bishop can move diagonally to d2

def test_pawn_moves():
    """Test that the Pawn moves correctly."""
    pawn = Pawn('white')
    board = initialize_board()
    moves = pawn.possible_moves(board, 6, 0)  # Pawn's position is a7 (row 6, col 0)
    assert (5, 0) in moves  # Pawn can move one square forward

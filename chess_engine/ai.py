import pytest
from chess_engine.game import Game
from chess_engine.ai import AI

def test_checkmate_scenario():
    """Test a checkmate situation."""
    game = Game()
    # Set up a checkmate position
    game.board[4][4] = 'k'  # Black King
    game.board[5][5] = 'Q'  # White Queen
    game.board[7][7] = 'K'  # White King
    result = game.check_game_over()
    assert result == 'checkmate', "Game should be over due to checkmate"

def test_pawn_promotion():
    """Test pawn promotion logic."""
    game = Game()
    # Move pawn to the 8th row and check if promotion happens
    game.board[6][0] = 'P'  # Place a white pawn at the 7th row
    game.move_piece(6, 0, 7, 0)  # White pawn moves to the 8th row
    assert game.board[7][0] == 'Q', "White pawn should be promoted to a Queen"

def test_stalemate():
    """Test a stalemate situation."""
    game = Game()
    # Set up a stalemate position
    game.board[0][0] = 'k'  # Black King
    game.board[1][2] = 'K'  # White King
    game.board[2][1] = 'Q'  # White Queen
    result = game.check_game_over()
    assert result == 'stalemate', "Game should be over due to stalemate"

def test_invalid_move():
    """Test an invalid move."""
    game = Game()
    # Attempt to move a piece from an empty square
    result = game.move_piece(4, 4, 5, 5)
    assert result == False, "Move should be invalid as there is no piece at the starting position"

def test_valid_move():
    """Test a valid move."""
    game = Game()
    # Move a white pawn forward
    result = game.move_piece(6, 0, 5, 0)
    assert result == True, "Move should be valid"
    assert game.board[5][0] == 'P', "Pawn should be moved to the new position"
    assert game.board[6][0] == ' ', "Original position should be empty"

def test_check():
    """Test a check situation."""
    game = Game()
    # Set up a check position
    game.board[4][4] = 'k'  # Black King
    game.board[5][5] = 'Q'  # White Queen
    result = game.is_in_check('black')
    assert result == True, "Black King should be in check"

def test_no_check():
    """Test a no check situation."""
    game = Game()
    # Set up a position where the king is not in check
    game.board[4][4] = 'k'  # Black King
    game.board[5][5] = 'P'  # White Pawn
    result = game.is_in_check('black')
    assert result == False, "Black King should not be in check"

if __name__ == "__main__":
    pytest.main()
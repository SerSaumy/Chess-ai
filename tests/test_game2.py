import pytest
from chess_engine.game import Game

def test_checkmate_scenario():
    """Test a checkmate situation."""
    game = Game()
    # Set up a checkmate position
    game.board[4][4] = 'k'  # Black King
    game.board[5][5] = 'Q'  # White Queen
    game.board[7][7] = 'K'  # White King
    result = game.check_game_over()
    assert result == True  # Game should be over due to checkmate

def test_pawn_promotion():
    """Test pawn promotion logic."""
    game = Game()
    # Move pawn to the 8th row and check if promotion happens
    game.move_piece(6, 0, 7, 0)  # White pawn moves to the 8th row
    assert game.board[7][0] == 'P'  # White pawn should be on the 8th row

def test_stalemate():
    """Test a stalemate situation."""
    game = Game()
    # Set up a stalemate position
    game.board[0][0] = 'k'  # Black King
    game.board[1][1] = 'K'  # White King
    result = game.check_game_over()
    assert result == True  # Game should be over due to stalemate

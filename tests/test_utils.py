# tests/test_utils.py

import unittest
from chess_engine.moves import generate_rook_moves, generate_knight_moves, generate_bishop_moves, generate_queen_moves, generate_king_moves, generate_pawn_moves
from chess_engine.board import initialize_board

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Initialize an empty board for the utility functions to work on
        self.board = initialize_board()

    def test_generate_rook_moves(self):
        # Test rook's moves from a specific position (e.g., (0, 0) with no obstacles)
        rook_moves = generate_rook_moves(self.board, 0, 0)
        self.assertIn((0, 1), rook_moves, "Rook should be able to move to (0, 1)")
        self.assertIn((1, 0), rook_moves, "Rook should be able to move to (1, 0)")
        
    def test_generate_knight_moves(self):
        # Test knight's moves from a specific position (e.g., (7, 1))
        knight_moves = generate_knight_moves(self.board, 7, 1)
        self.assertIn((5, 0), knight_moves, "Knight should be able to move to (5, 0)")
        self.assertIn((5, 2), knight_moves, "Knight should be able to move to (5, 2)")

    def test_generate_bishop_moves(self):
        # Test bishop's moves from a specific position (e.g., (2, 2))
        bishop_moves = generate_bishop_moves(self.board, 2, 2)
        self.assertIn((3, 3), bishop_moves, "Bishop should be able to move to (3, 3)")
        self.assertIn((1, 1), bishop_moves, "Bishop should be able to move to (1, 1)")

    def test_generate_queen_moves(self):
        # Test queen's moves from a specific position (e.g., (0, 3))
        queen_moves = generate_queen_moves(self.board, 0, 3)
        self.assertIn((0, 4), queen_moves, "Queen should be able to move to (0, 4)")
        self.assertIn((1, 3), queen_moves, "Queen should be able to move to (1, 3)")

    def test_generate_king_moves(self):
        # Test king's moves from a specific position (e.g., (7, 4))
        king_moves = generate_king_moves(self.board, 7, 4)
        self.assertIn((6, 3), king_moves, "King should be able to move to (6, 3)")
        self.assertIn((6, 4), king_moves, "King should be able to move to (6, 4)")

    def test_generate_pawn_moves(self):
        # Test pawn's moves from a specific position (e.g., (6, 0))
        pawn_moves = generate_pawn_moves(self.board, 6, 0)
        self.assertIn((5, 0), pawn_moves, "Pawn should be able to move to (5, 0)")
        self.assertIn((4, 0), pawn_moves, "Pawn should be able to move to (4, 0)")

if __name__ == "__main__":
    unittest.main()

# tests/test_ai.py

import unittest
from chess_engine.ai import AI
from chess_engine.board import initialize_board

class TestAI(unittest.TestCase):

    def setUp(self):
        # Initialize an empty board for the AI to play on
        self.board = initialize_board()
        # Initialize the AI with white pieces
        self.ai = AI(color='white')

    def test_evaluate_board(self):
        # Test the board evaluation method
        # For simplicity, let's assume that the white pawns have value 1 and the black pawns have value -1
        # Initial board evaluation should be 0 (balanced)
        score = self.ai.evaluate_board(self.board)
        self.assertEqual(score, 0, "Initial board evaluation should be 0")

    def test_get_best_move(self):
        # Test the AI's ability to pick the best move
        # Assuming the AI will try to capture the black pawn if possible
        possible_moves = [
            (6, 0, 5, 0),  # White pawn moves forward
            (6, 1, 5, 1),  # White pawn moves forward
        ]
        
        best_move = self.ai.get_best_move(self.board, possible_moves)
        # Test if the AI picks the first move (this is an example and would depend on your logic)
        self.assertEqual(best_move, (6, 0, 5, 0), "AI should choose the best move")

    def test_make_move(self):
        # Test the AI's ability to make a move
        # Example: Let the AI move its white pawn
        self.ai.make_move(self.board, [(6, 0, 5, 0)])  # White pawn moves forward
        self.assertEqual(self.board[5][0], 'P', "AI move not correctly applied to the board")
        self.assertEqual(self.board[6][0], ' ', "AI move not correctly applied to the board")
        
if __name__ == "__main__":
    unittest.main()

import unittest
from chess_engine.ai import AI
from chess_engine.board import initialize_board, print_board

class TestAI(unittest.TestCase):

    def setUp(self):
        self.board = initialize_board()
        self.ai = AI(color='white')

    def test_evaluate_board(self):
        score = self.ai.evaluate_board(self.board)
        self.assertIsNotNone(score, "Board evaluation should return a score")

    def test_get_best_move(self):
        best_move = self.ai.get_best_move(self.board)
        self.assertIsNotNone(best_move, "AI should return a best move")

    def test_make_move(self):
        self.ai.make_move(self.board)
        print_board(self.board)

if __name__ == "__main__":
    unittest.main()
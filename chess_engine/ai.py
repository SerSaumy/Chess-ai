# chess_engine/ai.py

import random
from .board import print_board

class AI:
    def __init__(self, color):
        self.color = color  # Color of the AI ('white' or 'black')

    def evaluate_board(self, board):
        """Evaluate the board based on material value."""
        piece_values = {
            'p': 1, 'P': -1,  # Pawn
            'n': 3, 'N': -3,  # Knight
            'b': 3, 'B': -3,  # Bishop
            'r': 5, 'R': -5,  # Rook
            'q': 9, 'Q': -9,  # Queen
            'k': 0, 'K': 0,   # King (no material value for checkmate)
        }
        
        score = 0
        for row in board:
            for cell in row:
                if cell != ' ':
                    score += piece_values.get(cell, 0)
        
        return score

    def get_best_move(self, board, possible_moves):
        """Choose the best move for the AI using a simple strategy."""
        best_move = None
        best_score = float('-inf')

        for start_row, start_col, end_row, end_col in possible_moves:
            # Simulate the move
            temp_board = [row[:] for row in board]  # Make a copy of the board
            temp_board[end_row][end_col] = temp_board[start_row][start_col]
            temp_board[start_row][start_col] = ' '

            # Evaluate the new board after the move
            score = self.evaluate_board(temp_board)

            # Select the move with the highest score
            if score > best_score:
                best_score = score
                best_move = (start_row, start_col, end_row, end_col)

        return best_move

    def make_move(self, board, possible_moves):
        """AI makes a move based on evaluation of the board."""
        best_move = self.get_best_move(board, possible_moves)
        
        if best_move:
            start_row, start_col, end_row, end_col = best_move
            board[end_row][end_col] = board[start_row][start_col]
            board[start_row][start_col] = ' '  # Empty the starting square

            print(f"AI ({self.color}) moves: {start_row} {start_col} -> {end_row} {end_col}")
            print_board(board)  # Print updated board after AI's move
        else:
            print("AI has no valid moves.")

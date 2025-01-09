
from chess_engine.board import initialize_board, print_board  # Use absolute import
from .moves import generate_rook_moves, generate_knight_moves, generate_bishop_moves, generate_queen_moves, generate_king_moves, generate_pawn_moves
from .utils import is_king_in_check, get_all_valid_moves  # Import utility functions for check and stalemate logic

class Game:
    def __init__(self):
        self.board = initialize_board()  # Initialize the board
        self.turn = 'white'  # White starts
        self.game_over = False  # Game is not over at the start

    def switch_turn(self):
        """Switch turns after each move."""
        self.turn = 'black' if self.turn == 'white' else 'white'

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """Check if the move is valid based on the current player's turn."""
        piece = self.board[start_row][start_col]
        target_piece = self.board[end_row][end_col]
        
        if piece == ' ':
            return False  # No piece at start location
        
        # Check if piece is the player's color
        if (self.turn == 'white' and piece.islower()) or (self.turn == 'black' and piece.isupper()):
            return False  # Wrong player's turn
        
        # Ensure not moving to a square occupied by the same color
        if target_piece != ' ' and (target_piece.islower() == piece.islower()):
            return False  # Can't capture your own piece
        
        return True

    def get_possible_moves(self, row, col):
        """Generate all possible moves for the piece at position (row, col)."""
        piece = self.board[row][col]
        
        if piece == ' ':
            return []
        
        if piece.lower() == 'r':
            return generate_rook_moves(self.board, row, col)
        elif piece.lower() == 'n':
            return generate_knight_moves(self.board, row, col)
        elif piece.lower() == 'b':
            return generate_bishop_moves(self.board, row, col)
        elif piece.lower() == 'q':
            return generate_queen_moves(self.board, row, col)
        elif piece.lower() == 'k':
            return generate_king_moves(self.board, row, col)
        elif piece.lower() == 'p':
            return generate_pawn_moves(self.board, row, col)

        return []

    def move_piece(self, start_row, start_col, end_row, end_col):
        """Move a piece and handle game state."""
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            print("Invalid move. Try again.")
            return False

        # Move the piece
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '  # Clear the starting position
        
        # Switch turn
        self.switch_turn()
        
        # Print updated board
        print_board(self.board)
        
        return True

    def check_game_over(self):
        """Check if the game is over (checkmate or stalemate)."""
        if is_king_in_check(self.board, self.turn):
            if not get_all_valid_moves(self.board, self.turn):
                return 'checkmate'  # Game over, checkmate
        elif not get_all_valid_moves(self.board, self.turn):
            return 'stalemate'  # Game over, stalemate

        return False

    def start_game(self):
        """Start the game and handle turns until the game ends."""
        while not self.game_over:
            print(f"\n{self.turn.capitalize()}'s Turn:")
            print_board(self.board)

            # Get user input (for simplicity)
            try:
                start_row, start_col = map(int, input("Enter the starting position (row col): ").split())
                end_row, end_col = map(int, input("Enter the ending position (row col): ").split())

                if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
                    print("Invalid board coordinates. Try again.")
                    continue

                if self.move_piece(start_row, start_col, end_row, end_col):
                    # Check if game is over after the move
                    result = self.check_game_over()
                    if result == 'checkmate':
                        print(f"{self.turn.capitalize()} is in checkmate! Game over.")
                        self.game_over = True
                    elif result == 'stalemate':
                        print(f"{self.turn.capitalize()} is in stalemate! Game over.")
                        self.game_over = True

            except ValueError:
                print("Invalid input. Please enter valid row and column numbers.")

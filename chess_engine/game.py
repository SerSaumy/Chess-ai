from chess_engine.board import initialize_board, print_board
from chess_engine.ai import AI

class Game:
    def __init__(self):
        self.board = initialize_board()
        self.turn = 'white'
        self.game_over = False
        self.ai_white = AI('white')
        self.ai_black = AI('black')

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        target_piece = self.board[end_row][end_col]
        if piece == ' ':
            return False
        if (self.turn == 'white' and piece.islower()) or (self.turn == 'black' and piece.isupper()):
            return False
        if target_piece != ' ' and (target_piece.islower() == piece.islower()):
            return False
        return True

    def move_piece(self, start_row, start_col, end_row, end_col):
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            print("Invalid move. Try again.")
            return False
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '
        if piece.lower() == 'p' and (end_row == 0 or end_row == 7):
            self.board[end_row][end_col] = 'Q' if piece.isupper() else 'q'
        self.switch_turn()
        print_board(self.board)
        result = self.check_game_over()
        if result == 'checkmate':
            print(f"{self.turn.capitalize()} is in checkmate! Game over.")
            self.game_over = True
        elif result == 'stalemate':
            print(f"{self.turn.capitalize()} is in stalemate! Game over.")
            self.game_over = True
        return True

    def is_in_check(self, color):
        king_position = self.find_king(color)
        return self.is_under_attack(king_position, color)

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece.lower() == 'k' and ((piece.isupper() and color == 'white') or (piece.islower() and color == 'black')):
                    return row, col
        return None

    def is_under_attack(self, position, color):
        opponent_color = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ' and ((piece.isupper() and opponent_color == 'white') or (piece.islower() and opponent_color == 'black')):
                    possible_moves = self.get_possible_moves(row, col)
                    if position in possible_moves:
                        return True
        return False

    def get_possible_moves(self, row, col):
        piece = self.board[row][col]
        if piece == ' ':
            return []
        if piece.lower() == 'r':
            return self.ai_white.generate_rook_moves(self.board, row, col)
        elif piece.lower() == 'n':
            return self.ai_white.generate_knight_moves(self.board, row, col)
        elif piece.lower() == 'b':
            return self.ai_white.generate_bishop_moves(self.board, row, col)
        elif piece.lower() == 'q':
            return self.ai_white.generate_queen_moves(self.board, row, col)
        elif piece.lower() == 'k':
            return self.ai_white.generate_king_moves(self.board, row, col)
        elif piece.lower() == 'p':
            return self.ai_white.generate_pawn_moves(self.board, row, col)
        return []

    def check_game_over(self):
        if self.is_in_check(self.turn):
            if not self.get_all_valid_moves(self.turn):
                self.game_over = True
                return 'checkmate'
        elif not self.get_all_valid_moves(self.turn):
            self.game_over = True
            return 'stalemate'
        return 'continue'

    def get_all_valid_moves(self, color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (color == 'white' and piece.isupper()) or (color == 'black' and piece.islower()):
                    possible_moves = self.get_possible_moves(row, col)
                    for move in possible_moves:
                        if self.is_valid_move(row, col, move[0], move[1]):
                            valid_moves.append((row, col, move[0], move[1]))
        return valid_moves

    def start_game(self):
        while not self.game_over:
            print(f"\n{self.turn.capitalize()}'s Turn:")
            print_board(self.board)
            try:
                start_row, start_col = map(int, input("Enter the starting position (row col): ").split())
                end_row, end_col = map(int, input("Enter the ending position (row col): ").split())
                if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
                    print("Invalid board coordinates. Try again.")
                    continue
                if self.move_piece(start_row, start_col, end_row, end_col):
                    result = self.check_game_over()
                    if result == 'checkmate':
                        print(f"{self.turn.capitalize()} is in checkmate! Game over.")
                        self.game_over = True
                    elif result == 'stalemate':
                        print(f"{self.turn.capitalize()} is in stalemate! Game over.")
                        self.game_over = True
            except ValueError:
                print("Invalid input. Please enter valid row and column numbers.")
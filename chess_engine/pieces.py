from chess_engine.moves import generate_king_moves, generate_queen_moves, generate_bishop_moves, generate_knight_moves, generate_rook_moves, generate_pawn_moves

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"{self.color[0].upper()}{self.__class__.__name__[0].upper()}"

    def possible_moves(self, board, row, col):
        raise NotImplementedError("This method should be implemented by subclasses.")

class King(Piece):
    def possible_moves(self, board, row, col):
        return generate_king_moves(board, row, col)

class Queen(Piece):
    def possible_moves(self, board, row, col):
        return generate_queen_moves(board, row, col)

class Bishop(Piece):
    def possible_moves(self, board, row, col):
        return generate_bishop_moves(board, row, col)

class Knight(Piece):
    def possible_moves(self, board, row, col):
        return generate_knight_moves(board, row, col)

class Rook(Piece):
    def possible_moves(self, board, row, col):
        return generate_rook_moves(board, row, col)

class Pawn(Piece):
    def possible_moves(self, board, row, col):
        return generate_pawn_moves(board, row, col)

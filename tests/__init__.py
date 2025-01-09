# tests/__init__.py

import pytest  # Import the pytest testing framework

# Setup for pytest or other testing frameworks can be placed here

@pytest.fixture(scope="module")
def setup_board():
    """Fixture to initialize the chessboard."""
    from chess_engine.board import initialize_board  # Import the board setup function
    board = initialize_board()  # Initialize the chessboard
    return board  # Return the initialized board to be used in tests

@pytest.fixture(scope="module")
def setup_game():
    """Fixture to initialize the game."""
    from chess_engine.game import Game  # Import the Game class
    game = Game()  # Initialize the game
    return game  # Return the initialized game to be used in tests

@pytest.fixture(scope="module")
def setup_ai():
    """Fixture to initialize the AI."""
    from chess_engine.ai import AI  # Import the AI class
    ai_white = AI('white')  # Initialize AI for white
    ai_black = AI('black')  # Initialize AI for black
    return ai_white, ai_black  # Return both AI instances to be used in tests

@pytest.fixture(scope="function")
def setup_custom_board():
    """Fixture to set up a custom board state."""
    def _setup_custom_board(custom_setup):
        from chess_engine.board import initialize_board
        board = initialize_board()
        for position, piece in custom_setup.items():
            row, col = position
            board[row][col] = piece
        return board
    return _setup_custom_board
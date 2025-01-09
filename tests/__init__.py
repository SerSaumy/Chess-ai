# tests/__init__.py

import pytest  # Import the pytest testing framework

# Setup for pytest or other testing frameworks can be placed here

# Example setup: Set up a basic fixture that you can use across tests
@pytest.fixture(scope="module")  # Creates a setup fixture for the whole module
def setup_game():
    from chess_engine.board import initialize_board  # Import the board setup function
    board = initialize_board()  # Initialize the chessboard
    return board  # Return the initialized board to be used in tests

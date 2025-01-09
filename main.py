from chess_engine.game import Game
from chess_engine.board import initialize_board

def main():
    # Initialize the board
    board = initialize_board()

    # Create a new game instance
    game = Game(board)

    print("Welcome to the Chess Game!")

    # Main game loop
    while True:
        # Print the current board state
        game.print_board()

        # Get current player's move
        move = input(f"{game.current_turn}'s move (e.g., e2e4): ")

        if move.lower() == 'quit':
            print("Game Over!")
            break

        # Apply the move to the game
        if game.make_move(move):
            print(f"Move {move} made successfully.")
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()

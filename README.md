# Chess AI Project

Welcome to the Chess AI project! This project is a simple implementation of a chess game where you can play against a basic AI. The AI makes decisions based on piece values and a basic evaluation function. The game includes all standard chess rules and pieces, allowing a human player to enjoy a full game of chess with an AI opponent.

## Table of Contents
1. Introduction
2. Installation
3. Usage
4. Project Structure
5. License
6. Acknowledgments

## Introduction
This project provides a Python-based implementation of a chess game that includes a chess-playing AI. The AI uses a basic evaluation function that compares the material balance between the two players. It can play as both white and black pieces and offers a fun, though simple, experience for chess enthusiasts.

The game logic supports standard chess rules such as piece movement, captures, and turns. The AI is designed to make moves by evaluating the board, considering the value of the pieces, and choosing the best move accordingly.

### Features:
- Play chess against a simple AI.
- Supports all chess pieces with their proper movement.
- A basic AI that evaluates piece values to make decisions.
- Board validation and turn management.
- Interactive gameplay through the terminal.

## Installation
To get started with the Chess AI project, follow these steps:

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/SerSaumy/Chess-ai.git
   ```

2. **Navigate into the project directory**:
   ```bash
   cd Chess-ai
   ```

3. **Install the required Python dependencies**:
   If you have `pip` installed, you can install all necessary libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Optional: Set up a virtual environment** (recommended for isolated development):
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

5. **You're all set to play!**

## Usage
Once the project is installed and set up, you can run the game. Follow these steps:

1. **Start the game** by running the `main.py` file:
   ```bash
   python main.py
   ```

2. **Interactive gameplay** will begin, and you'll be prompted to enter your moves in the format of two coordinates: the starting and ending positions of your pieces (e.g., `0 1` to `2 1`).

3. **Game flow**:
   - The game will alternate between the human player and the AI.
   - The AI will make its move after you input yours.
   - The game will notify you if it's your turn, and it will also check for checkmate or stalemate situations.

4. To run tests and ensure the code works as expected, simply run:
   ```bash
   pytest
   ```

## Project Structure
Here’s a quick overview of the project structure:

```
Chess-ai/
├── chess_engine/               # Core engine for the chess game
│   ├── ai.py                   # AI logic for deciding moves
│   ├── board.py                # Board initialization and display
│   ├── game.py                 # Game management and move validation
│   ├── pieces.py               # Chess piece classes and movements
│   └── utils.py                # Utility functions for game operations
├── tests/                      # Unit tests for various game functionalities
│   ├── test_ai.py              # AI logic unit tests
│   ├── test_game.py            # Game logic unit tests
│   ├── test_utils.py           # Utility functions unit tests
│   └── test_pieces.py          # Piece movement unit tests
├── .gitignore                  # Ignored files for version control
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── main.py                     # Entry point for the chess game
```

### Key Files:
- **`chess_engine/ai.py`**: Contains the AI logic that evaluates board positions and makes moves based on piece values.
- **`chess_engine/game.py`**: Manages the game flow, turn-taking, and validates moves.
- **`chess_engine/pieces.py`**: Defines the classes for all chess pieces (King, Queen, Rook, etc.) and their movement patterns.
- **`tests/`**: Contains unit tests to verify the correctness of the game, AI, and utilities.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
- **Python**: For providing an easy-to-learn, powerful language for building this project.
- **Chess community**: For the countless contributions, strategies, and algorithms shared over the years that helped shape chess AI.
- **Open source contributors**: For providing various libraries and tools that made this project possible.
- **You**: For checking out and using this project!

---

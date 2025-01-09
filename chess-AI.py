# This is a comment. Comments are ignored by the computer. They're for us to understand the code.

def initialize_board(): # This defines a function called initialize_board
    board = [ # This creates a list of lists, which represents the board
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], # Row 0 (Black's back rank)
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], # Row 1 (Black's pawns)
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # Row 2 (Empty)
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # Row 3 (Empty)
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # Row 4 (Empty)
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # Row 5 (Empty)
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # Row 6 (White's pawns)
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # Row 7 (White's back rank)
    ]
    return board # This line makes the function "give back" the board so we can use it later

def print_board(board): # This defines a function to print the board neatly
    for row in board: # This loops through each row of the board
        print(" ".join(row)) # This prints the row with spaces between each piece

def generate_rook_moves(board, row, col):
    moves = []
    for i in range(row + 1, 8): #down
        if board[i][col] == ' ':
            moves.append((i, col))
        else:
            break
    for i in range(row - 1, -1, -1): #up
        if board[i][col] == ' ':
            moves.append((i, col))
        else:
            break
    for j in range(col + 1, 8): #right
        if board[row][j] == ' ':
            moves.append((row, j))
        else:
            break
    for j in range(col - 1, -1, -1): #left
        if board[row][j] == ' ':
            moves.append((row, j))
        else:
            break
    return moves

# Example of how to use the functions:
board = initialize_board() # This calls the function and stores the result in the variable 'board'
print_board(board) # This prints the board to the console
rook_moves = generate_rook_moves(board, 7, 0)
print("Possible rook moves: ", rook_moves)

board[7][0] = ' '
board[5][0] = 'R'
print_board(board)
rook_moves = generate_rook_moves(board, 5, 0)
print("Possible rook moves: ", rook_moves)
import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print(board[3*i] + ' | ' + board[3*i+1] + ' | ' + board[3*i+2])
        if i < 2:
            print('--+---+--')

# Check for winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full():
    return ' ' not in board

# Human move
def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
        print("Invalid move. Try again.")

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Minimax function
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner('X'):
            print("You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner('O'):
            print("AI wins!")
            break
        if is_full():
            print("It's a draw!")
            break

# Start the game
play_game()

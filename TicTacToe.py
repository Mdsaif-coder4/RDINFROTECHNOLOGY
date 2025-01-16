import math
board = [" " for _ in range(9)]
def display_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-+-+-")
def check_winner(board):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Tie"
    return None
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                return move
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
def minimax(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Tie":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    player = input("Choose X or O: ").upper()
    ai = "O" if player == "X" else "X"

    for turn in range(9):
        display_board()
        if (turn % 2 == 0 and player == "X") or (turn % 2 == 1 and player == "O"):
            move = human_move()
            board[move] = player
        else:
            move = ai_move()
            print(f"AI chooses position {move + 1}")
            board[move] = ai

        winner = check_winner(board)
        if winner:
            display_board()
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

play_game()
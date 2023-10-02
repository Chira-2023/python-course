# this code copy by chat gpt-3



def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True, board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True, board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True, board[0]
    if board[2] == board[4] == board[6] != " ":
        return True, board[2]
    # Check if board is full
    if " " not in board:
        return True, "Tie"
    # No winner yet
    return False, ""

def get_move(player, board):
    while True:
        move = input(f"{player}'s turn (X or O): ")
        if move.isdigit() and int(move) >= 1 and int(move) <= 9:
            index = int(move) - 1
            if board[index] == " ":
                return index
        print("Invalid move. Try again.")

def play_game():
    board = [" "]*9
    print_board(board)
    current_player = "X"
    while True:
        move = get_move(current_player, board)
        board[move] = current_player
        print_board(board)
        winner_found, winner = check_winner(board)
        if winner_found:
            if winner == "Tie":
                print("Tie game!")
            else:
                print(f"{winner} wins!")
            break
        current_player = "O" if current_player == "X" else "X"

play_game()

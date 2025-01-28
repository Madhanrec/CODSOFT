
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    if all(cell != " " for row in board for cell in row):
        return "Draw"
    return None


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print_board(board)

    while True:
        try:
            row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
            else:
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 0 and 2.")
            continue

        print_board(board)
        if check_winner(board):
            print(f"Game Over! Winner: {check_winner(board)}")
            break

       
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = "O"

        print_board(board)
        if check_winner(board):
            print(f"Game Over! Winner: {check_winner(board)}")
            break

if __name__ == "__main__":
    main()
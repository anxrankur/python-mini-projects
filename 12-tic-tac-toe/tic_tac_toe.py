board = [" " for _ in range(9)]

def show_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_combinations
    )


print("===== TIC-TAC-TOE =====")
print("Player 1: X")
print("Player 2: O")
print("Choose positions from 1 to 9.")

current_player = "X"
moves = 0

while True:
    show_board()

    try:
        position = int(input(f"Player {current_player}, choose a position: ")) - 1

        if position < 0 or position > 8:
            print("❌ Choose a number from 1 to 9.")
            continue

        if board[position] != " ":
            print("❌ That position is already taken.")
            continue

    except ValueError:
        print("❌ Please enter a number.")
        continue

    board[position] = current_player
    moves += 1

    if check_winner(current_player):
        show_board()
        print(f"🎉 Player {current_player} wins!")
        break

    if moves == 9:
        show_board()
        print("🤝 It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"

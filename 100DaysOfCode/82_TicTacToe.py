""" Día 82: Implementar tres en raya
Implementar un juego (por ejemplo, Tic-Tac-Toe, Hangman) en Python. """

import random
import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tic-Tac-Toe")
    print("Player 1 (X)  -  Player 2 (O)")
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()
def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter your row (0-2): "))
            col = int(input(f"Player {current_player}, enter your column (0-2): "))
            if board[row][col] != ' ':
                print("Cell already taken, try again.")
                continue
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid input, please enter numbers between 0 and 2.")
if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
Program to solve the N queens problem.
"""
import sys


def find_queen_positions(row, size, used_columns, positive_diagonals, negative_diagonals, chess_board):
    """
    Recursively attempts to find all valid queen positions on the chessboard.
    """
    if row == size:
        solution = []
        for i in range(size):
            for j in range(size):
                if chess_board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(size):
        if col in used_columns or (row + col) in positive_diagonals or (row - col) in negative_diagonals:
            continue

        used_columns.add(col)
        positive_diagonals.add(row + col)
        negative_diagonals.add(row - col)
        chess_board[row][col] = 1

        find_queen_positions(row + 1, size, used_columns, positive_diagonals, negative_diagonals, chess_board)

        # Backtrack: remove the queen and reset the state
        used_columns.remove(col)
        positive_diagonals.remove(row + col)
        negative_diagonals.remove(row - col)
        chess_board[row][col] = 0


def nqueens_solver(n):
    """
    Finds and prints all solutions to the N queens problem.
    Args:
        n (int): Number of queens and the size of the chessboard (NxN).
    """
    used_columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    chess_board = [[0] * n for _ in range(n)]

    find_queen_positions(0, n, used_columns, positive_diagonals, negative_diagonals, chess_board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num_queens = int(sys.argv[1])
        if num_queens < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens_solver(num_queens)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


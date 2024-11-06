#!/usr/bin/python3
"""
Program to solve the N queens problem.
"""
import sys


def solve(row, n, cols, p_diag, n_diag, board):
    """
    Recursively find all solutions to the N queens problem.
    """
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(n):
        if col in cols or (row + col) in p_diag or (row - col) in n_diag:
            continue

        cols.add(col)
        p_diag.add(row + col)
        n_diag.add(row - col)
        board[row][col] = 1

        solve(row + 1, n, cols, p_diag, n_diag, board)

        # Backtrack
        cols.remove(col)
        p_diag.remove(row + col)
        n_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Print all solutions to the N queens problem.
    """
    cols = set()
    p_diag = set()
    n_diag = set()
    board = [[0] * n for _ in range(n)]

    solve(0, n, cols, p_diag, n_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

#!/usr/bin/python3
""" Solve the N queens problem """
import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
            board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n, board=[], col=0):
    if col == n:
        print(board)
        return

    for row in range(n):
        if is_safe(board, row, col):
            board.append(row)
            solve_nqueens(n, board, col + 1)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

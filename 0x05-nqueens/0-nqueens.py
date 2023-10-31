#!/usr/bin/python3
"""N-queens puzzle solver.

Finds all possible configurations of placing N non-attacking queens on an NxN chessboard.

Usage:
    $ ./0-nqueens.py N

Where N is an integer greater than or equal to 4.

Output:
    A list of configurations, where each configuration shows positions [r, c] of each queen.
"""
import sys


def init_board(n):
    """Create an NxN chessboard initialized with spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Create a deep copy of the board."""
    return [row[:] for row in board]


def get_solution(board):
    """Extract the positions of queens from the board."""
    return [[r, c] for r, row in enumerate(board) for c, val in enumerate(row) if val == "Q"]


def xout(board, row, col):
    """Mark positions on the board that are under attack from a queen at (row, col)."""
    size = len(board)
    for i in range(size):
        # Horizontal and vertical positions
        board[row][i], board[i][col] = "x", "x"
        # Diagonal positions
        if 0 <= row + i < size and 0 <= col + i < size:
            board[row + i][col + i] = "x"
        if 0 <= row - i < size and 0 <= col - i < size:
            board[row - i][col - i] = "x"
        if 0 <= row + i < size and 0 <= col - i < size:
            board[row + i][col - i] = "x"
        if 0 <= row - i < size and 0 <= col + i < size:
            board[row - i][col + i] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively search for solutions."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)

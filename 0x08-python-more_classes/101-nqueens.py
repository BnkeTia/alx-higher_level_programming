import sys
"""
The queens code.
"""


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in the given position.

    Args:
        board (list[list[int]]): The chessboard.
        row (int): The current row.
        col (int): The current column.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print solutions.

    Args:
        n (int): The size of the chessboard.
    """
    if n < 4:
        return

    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(row):
        if row == n:
            for i in range(n):
                print("".join(['Q' if board[row][i] == 1
                              else '.' for i in range(n)]))
            print()
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    except IndexError:
        print("N must be at least 4")
        sys.exit(1)

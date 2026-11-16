"""
Assignment 5: n-Queens with the first queen already placed.
Backtracking places the remaining queens.

Time complexity : O(n!) in the worst case
Space complexity: O(n) for the bookkeeping sets + O(n^2) for the board
"""


def solve_n_queens(n, first_row, first_col):
    """Returns the board (list of lists) or None if no solution exists."""
    board = [[0] * n for _ in range(n)]
    cols = set()
    diag1 = set()   # row - col is constant on a "\" diagonal
    diag2 = set()   # row + col is constant on a "/" diagonal

    def place(r, c):
        board[r][c] = 1
        cols.add(c)
        diag1.add(r - c)
        diag2.add(r + c)

    def remove(r, c):
        board[r][c] = 0
        cols.discard(c)
        diag1.discard(r - c)
        diag2.discard(r + c)

    def is_safe(r, c):
        return c not in cols and (r - c) not in diag1 and (r + c) not in diag2

    def backtrack(row):
        if row == n:
            return True
        if row == first_row:              # this row already has the first queen
            return backtrack(row + 1)
        for col in range(n):
            if is_safe(row, col):
                place(row, col)
                if backtrack(row + 1):
                    return True
                remove(row, col)          # backtrack
        return False

    place(first_row, first_col)
    return board if backtrack(0) else None


def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def main():
    n = int(input("Enter number of queens (n): "))
    row = int(input(f"Enter row of first queen    (1 to {n}): "))
    col = int(input(f"Enter column of first queen (1 to {n}): "))

    if n < 1 or not (1 <= row <= n and 1 <= col <= n):
        print("Invalid input")
        return

    board = solve_n_queens(n, row - 1, col - 1)

    if board is None:
        print(f"\nNo solution exists with the first queen at ({row}, {col}).")
    else:
        print(f"\nFinal {n}-Queens matrix (first queen at ({row}, {col})):\n")
        print_board(board)
        print("\nAs 0/1 matrix:")
        for r in board:
            print(*r)


if __name__ == "__main__":
    main()

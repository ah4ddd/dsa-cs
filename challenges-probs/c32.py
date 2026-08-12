# C32 -- Valid Sudoku

from collections import defaultdict

def is_valid_sudoku(board):
    # The dictionary owns the key-value pair.
    # The value happens to be a set.
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])

    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

result = is_valid_sudoku(board)
print(result)


"""
                    CELL
                     │
                     ↓
              ┌──────┼──────┐
              ↓      ↓      ↓
            ROW    COLUMN   BOX
              │      │      │
              ↓      ↓      ↓
             SET    SET     SET
              │      │      │
              └──────┼──────┘
                     ↓
              duplicate?
               /        \
             YES         NO
              ↓           ↓
           FALSE       add to sets
"""


# SOL 2
def is_valid_sudoku_(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):

            if board[r][c] == ".":
                continue

            num = board[r][c]

            square = (r // 3) * 3 + (c // 3)

            if num in rows[r] or num in cols[c] or num in squares[square]:
                return False

            rows[r].add(num)
            cols[c].add(num)
            squares[square].add(num)

    return True


# BRUTE FORCE
class Solution:
    def isValidSudoku(self, board):

        # Check rows
        for r in range(9):
            seen = set()

            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # Check columns
        for c in range(9):
            seen = set()

            for r in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # Check 3x3 squares
        for box_row in range(3):
            for box_col in range(3):
                seen = set()

                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in seen:
                            return False

                        seen.add(board[r][c])

        return True

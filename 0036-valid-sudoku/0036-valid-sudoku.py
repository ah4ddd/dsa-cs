class Solution:
    def isValidSudoku(self, board):
        seen = set()

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue

                row = (value, r)
                col = (c, value)
                box = (r // 3, c // 3, value)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        rows = len(mat)
        cols = len(mat[0])

        result = []

        r = 0 # → current row
        c = 0 # → current column
        direction = 1 # → which way we're moving

        while len(result) < rows * cols:

            result.append(mat[r][c])

            if direction == 1:       # moving up-right
                if c == cols - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1

            else:                    # moving down-left
                if r == rows - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result
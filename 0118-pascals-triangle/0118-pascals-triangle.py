class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1] # L1

            if result:
                previous = result[-1] 

                for j in range(len(previous) - 1):
                    # The engine
                    row.append(previous[j] + previous[j + 1])

                row.append(1) # R1

            result.append(row)

        return result
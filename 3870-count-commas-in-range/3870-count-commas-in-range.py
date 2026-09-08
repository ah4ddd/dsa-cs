class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) <= 3:
            return 0
        
        num = str(n)
        comma = 0

        for i in range(1000, n+1):
            comma += 1

        return comma
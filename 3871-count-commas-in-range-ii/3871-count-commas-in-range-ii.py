class Solution:
    def countCommas(self, n: int) -> int:
        r = 0
        p = 1000

        while p <= n:
            r += n - p + 1
            p *= 1000

        return r
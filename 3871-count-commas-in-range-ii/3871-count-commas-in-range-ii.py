class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        r = 0
        s = 1000
        c = 1

        while s <= n:
            end = min(n, s * 1000 - 1)
            r += (end - s + 1) * c

            s *= 1000
            c += 1

        return r
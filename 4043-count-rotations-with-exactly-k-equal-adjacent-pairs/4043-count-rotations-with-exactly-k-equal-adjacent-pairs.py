class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)

        t = sum(s[i] == s[(i + 1) % n] for i in range(n))

        ans = 0

        for i in range(n):
            removed = s[i - 1] == s[i]
            score = t - removed

            if score == k:
                ans += 1

        return ans
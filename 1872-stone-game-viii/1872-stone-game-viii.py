class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] + stones[i]
        
        dp = [0] * n
        best = prefix[n-1]
        
        for i in range(n-2, -1, -1):
            dp[i] = best
            best = max(best, prefix[i] - dp[i])
        
        return dp[0]
        
        
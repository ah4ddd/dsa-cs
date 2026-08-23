class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for todays in range(1, len(prices)):
            if prices[todays] > prices[todays - 1]:
                best += prices[todays] - prices[todays - 1]

        return best

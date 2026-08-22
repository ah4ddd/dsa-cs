class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0

        for price in prices:
            if price < lowest:
                lowest = price

            todays_profit = price - lowest

            if todays_profit > best:
                best = todays_profit

        if best <= 0:
            return 0

        return best
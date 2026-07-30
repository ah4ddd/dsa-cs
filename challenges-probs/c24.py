# Challenge 24 — Best Time to Buy and Sell Stock

# You're given the stock price for each day.
# prices = [7, 1, 5, 3, 6, 4]


"""
Each number represents:

Day 1 → 7
Day 2 → 1
Day 3 → 5
Day 4 → 3
Day 5 → 6
Day 6 → 4

You may:
    Buy once
    Sell once
    You must buy before you sell

Return the maximum profit.

Example:
    prices = [7,1,5,3,6,4]

Best decision:
    Buy at 1
    Sell at 6

Profit:
    6 - 1 = 5

Return
    5

Another Example
    prices = [7,6,4,3,1]

Prices only go down.

There is no profitable trade.

Return
    0

Not negative.

Just don't trade.
"""


prices = [5, 8, 1, 4, 6, 3]


def max_profit(prices):
    lowest = prices[0]
    best = 0

    buy = prices[0]
    sell = 0

    for p in prices:
        if p < lowest:
            lowest = p

        todays_profit = p - lowest

        if todays_profit > best:
            best = todays_profit
            buy = lowest
            sell = p

    print(f"Buy: {buy}")
    print(f"Sell: {sell}")
    print(f"Profit: {best}")

    if best <= 0:
        return 0
    return best


profit = max_profit(prices)

print(profit)


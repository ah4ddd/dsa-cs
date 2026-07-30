# Challenge 24 — Best Time to Buy and Sell Stock

prices = [5, 8, 1, 4, 6, 3]


def max_profit(prices):
    # Keep track of the cheapest price seen so far.
    lowest = prices[0]
    # Update the best profit found.
    best = 0

    buy = prices[0]
    sell = 0

    for p in prices:
        if p < lowest:
            lowest = p
        # Profit if we sold today.
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


# soluion from leetcode

prices = [3, 8, 1, 7, 6, 3]

def maxProfit(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit

profit = maxProfit(prices)

print(profit)


"""
Pattern:
    running minimum

    +

    running maximum (or best answer)


Whenever you process data in one pass, ask:

    What is the best thing I've seen so far?
    What is the worst thing I've seen so far?
    What is the smallest value so far?
    What is the largest value so far?

That thinking appears everywhere.
"""

# Challenge 24 — Best Time to Buy and Sell Stock

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


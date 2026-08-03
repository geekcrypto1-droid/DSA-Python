input = [7,1,5,3,6,4]

output = 7

def maxProfit(prices):
    small = prices[0]
    max_profit = 0

    for price in prices:
        small = min(price, small)
        profit = price - small
        max_profit = max(max_profit, profit)

    return max_profit

print(maxProfit(input))

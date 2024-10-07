"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(prices):
    i = 0
    while True:
        min_i = prices.index(min(prices))
        max_i = prices.index(max(prices))
        print(min_i)
        print(max_i)
        if max_i>min_i:
            return f'here it comes ->{prices[max_i]-prices[min_i]}'
            break
        else:
            prices.remove(prices[max_i+i])
            i += 1
        print(prices)

print(maxProfit([7,1,5,3,6,4]))


def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Track the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate potential profit if selling on this day
        potential_profit = price - min_price
        # Update the maximum profit if this potential profit is higher
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

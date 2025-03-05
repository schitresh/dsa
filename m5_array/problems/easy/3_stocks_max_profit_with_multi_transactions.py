from utils import test_class

# Given an array of size n for prices denoting the cost of stock on each day, find the
# maximum total profit if we can buy and sell the stocks any number of times.
# We can only sell a stock which we have bought earlier and we cannot hold multiple
# stocks on any day.

examples = [
  {
    'input': [[100, 180, 260, 310, 40, 535, 695]],
    'output': 865,
    # Buy the stock on day 0 and sell it on day 3: 310 - 100 = 210
    # Buy the stock on day 4 and sell it on day 6: 695 - 40 = 655
    # Maximum Profit: 210 + 655 = 865
  },
  {
    'input': [[4, 2, 2, 2, 4]],
    'output': 2,
    # Buy the stock on day 3 and sell it on day 4: 4 - 2 = 2
  },
]

# Local Minima and Maxima
# Buy when the prices drop to the lowest and start increasing after that
# Sell when the prices rise to the highest and start decreasing after that
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, prices):
    max_profit = 0
    buy_price = None

    for i in range(len(prices) - 1):
      if buy_price is None:
        if prices[i] < prices[i + 1]:
          buy_price = prices[i]
      else:
        if prices[i] > prices[i + 1]:
          max_profit += prices[i] - buy_price
          buy_price = None

    if buy_price:
      max_profit += prices[-1] - buy_price

    return max_profit

test_class(Solution, examples)

# Accumulate Profit
# Optimization of previous solution. Instead of selling at local maxima, keep selling
# while the prices are going up. This will accumulate the same profit and avoid
# condition checks for local minima and maxima.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, prices):
    max_profit = 0

    for i in range(1, len(prices)):
      if prices[i - 1] < prices[i]:
        max_profit += prices[i] - prices[i - 1]

    return max_profit

test_class(Solution2, examples)

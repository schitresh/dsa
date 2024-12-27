from utils import test_class

# In a stock market, there is a product with its infinite stocks. The stock prices are
# given for N days, where arr[i] denotes the price of the stock on the ith day. There is
# a rule that a customer can buy at most i stock on the ith day. If the customer has k
# amount of money initially, find out the maximum number of stocks a customer can buy.

examples = [
  {
    'input': [45, [10, 7, 19]], # amount, prices
    'output': 4,
    # One stock worth 10 rs on day 1
    # Two stocks worth 7 rs each on day 2
    # One stock worth 19 rs on day 3
  },
  {
    'input': [100, [7, 10, 4]],
    'output': 6,
    # One stock worth 7 rs on day 1
    # Two stocks worth 10 rs each on day 2
    # Three stocks worth 4 rs each on day 3
  }
]

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, amount, prices):
    prices_with_day = list(zip(prices, range(1, len(prices) + 1)))
    prices_with_day.sort()
    amt_left = amount
    count = 0

    for idx in range(len(prices)):
      price, day = prices_with_day[idx]
      capacity = amt_left // price

      stocks = min(day, capacity)
      count += stocks
      amt_left = amount - price * stocks

    return count

test_class(Solution, examples)

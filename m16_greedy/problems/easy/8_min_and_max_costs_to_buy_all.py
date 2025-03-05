from utils import test_class

# In a candy store, there are N different types of candies available and the prices of
# all the N different types of candies are provided. There is also an attractive offer
# by the candy store. We can buy a single candy from the store and get at most K other
# candies (all are different types) for free.
# Find the minimum and the maximum amount of money we have to spend to buy all the
# N different candies.
# In both cases, we must utilize the offer and get the maximum possible candies back.
# If k or more candies are available, we must take k candies for every candy purchase.
# If less than k candies are available, we must take all candies for a candy purchase.

examples = [
  {
    'input': [2, [3, 2, 1, 4]], # k, prices
    'output': [3, 7], # min, max
    # Since k is 2, if we buy one candy, we can take atmost two more for free.
    # So in the first case we buy the candy which costs 1 and take candies worth 3 and 4
    # for free. Also, we need to buy candy worth 2. So, min cost = 1 + 2 = 3.
    # In the second case, we buy the candy which costs 4 and take candies worth 1 and 2
    # for free. Also, we need to buy candy worth 3. So, max cost = 3 + 4 = 7.
  },
  {
    'input': [4, [3, 2, 1, 4, 5]],
    'output': [1, 5],
  }
]

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, free_candies, prices):
    prices.sort()

    min_cost = 0
    left = 0
    right = len(prices) - 1
    while left <= right:
      min_cost += prices[left]
      left += 1
      right -= free_candies

    max_cost = 0
    left = 0
    right = len(prices) - 1
    while left <= right:
      max_cost += prices[right]
      right -= 1
      left += free_candies

    return [min_cost, max_cost]

test_class(Solution, examples)

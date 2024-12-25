from utils import test_class

# There are N items where each item has some weight and profit associated with it
# There is also a bag with capacity W, i.e. the bag can hold at most W weight in it.
# Put the items into the bag such that the sum of profits associated with them is
# the maximum possible.
# The constraint here is that we can either put an item completely into the bag
# or cannot put it at all. It is not possible to put a part of an item.

examples = [
  {
    'input': [4, [1, 2, 3], [4, 5, 1]], # W (knapsack weight), profits, weights
    'output': 3, # Put the item with weight 1 & profit 3
  },
  {
    'input': [3, [1, 2, 3], [4, 5, 6]],
    'output': 0,
  },
  {
    'input': [60, [40, 100, 50, 60], [20, 10, 40, 30]],
    'output': 200,
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, knapsack_weight, profits, weights):
    self.profits = profits
    self.weights = weights

    return self.knapsack(0, knapsack_weight)

  def knapsack(self, pos, rem_weight):
    if pos == len(self.weights): return 0

    weight1 = rem_weight
    profit1 = self.knapsack(pos + 1, weight1)

    weight2 = rem_weight - self.weights[pos]
    profit2 = 0
    if weight2 >= 0:
      profit2 = self.profits[pos] + self.knapsack(pos + 1, weight2)

    return max(profit1, profit2)

test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(n * W)
# Auxiliary Space: O(n * W)
class Solution2:
  def solve(self, knapsack_weight, profits, weights):
    self.profits = profits
    self.weights = weights
    self.max_profit = [[None] * (knapsack_weight + 1) for _ in range(len(weights))]

    return self.knapsack(0, knapsack_weight)

  def knapsack(self, pos, rem_weight):
    if pos == len(self.weights): return 0

    if self.max_profit[pos][rem_weight]:
      return self.max_profit[pos][rem_weight]

    weight1 = rem_weight
    profit1 = self.knapsack(pos + 1, weight1)

    weight2 = rem_weight - self.weights[pos]
    profit2 = 0
    if weight2 >= 0:
      profit2 = self.profits[pos] + self.knapsack(pos + 1, weight2)

    self.max_profit[pos][rem_weight] = max(profit1, profit2)
    return self.max_profit[pos][rem_weight]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n * W)
# Auxiliary Space: O(n * W)
class Solution3:
  def solve(self, knapsack_weight, profits, weights):
    max_profit = [[0] * (knapsack_weight + 1) for _ in range(len(weights) + 1)]

    for pos in range(len(weights)):
      for weight in range(knapsack_weight + 1):
        weight1 = weight
        profit1 = max_profit[pos][weight1]

        weight2 = weight - weights[pos]
        profit2 = 0
        if weight2 >= 0:
          profit2 = profits[pos] + max_profit[pos][weight2]

        max_profit[pos + 1][weight] = max(profit1, profit2)

    return max_profit[len(weights)][knapsack_weight]

test_class(Solution3, examples)

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(n * W)
# Auxiliary Space: O(W)
class Solution4:
  def solve(self, knapsack_weight, profits, weights):
    max_profit = [0] * (knapsack_weight + 1)

    for pos in range(len(weights)):
      # Iterate backwards because we need the previous data of weight2
      # which is less than the current weight
      for weight in range(knapsack_weight, 0, -1):
        weight1 = weight
        profit1 = max_profit[weight1]

        weight2 = weight - weights[pos]
        profit2 = 0
        if weight2 >= 0:
          profit2 = profits[pos] + max_profit[weight2]

        max_profit[weight] = max(profit1, profit2)

    return max_profit[knapsack_weight]

test_class(Solution4, examples)

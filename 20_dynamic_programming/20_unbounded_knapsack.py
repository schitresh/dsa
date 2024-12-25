from utils import test_class

# Given a knapsack weight and a set of n items with certain value and weight,
# fill the knapsack in such a way that we can get the maximum profit.
# This is different from the classical Knapsack problem, here we are allowed to use
# an unlimited number of instances of an item.

examples = [
  {
    'input': [100, [1, 30], [1, 50]], # W (knapsack weight), profits, weights
    'output': 100,
    # Possible with 2 of weight 50, 100 of weight 1, 1 of weight 50 & 50 of weight 1
    # Maximum value in 100 of 1 weight
  },
  {
    'input': [8, [10, 40, 50, 70], [1, 3, 4, 5]],
    'output': 110, # 1 of weight 5 & 1 of weight 3
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
      # Unlike standard knapsack, not increasing pos to pos + 1
      # The first case will anyways handle that in the next iteration
      profit2 = self.profits[pos] + self.knapsack(pos, weight2)

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
      # Unlike standard knapsack, not increasing pos to pos + 1
      # The first case will anyways handle that in the next iteration
      profit2 = self.profits[pos] + self.knapsack(pos, weight2)

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
          profit2 = profits[pos] + max_profit[pos + 1][weight2]

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
      # In standard knapsack, we iterate backwards to avoid overriding data for weight2
      # But here we need the new data for weight2, so we need to override
      for weight in range(knapsack_weight + 1):
        weight1 = weight
        profit1 = max_profit[weight1]

        weight2 = weight - weights[pos]
        profit2 = 0
        if weight2 >= 0:
          profit2 = profits[pos] + max_profit[weight2]

        max_profit[weight] = max(profit1, profit2)

    return max_profit[knapsack_weight]

test_class(Solution4, examples)

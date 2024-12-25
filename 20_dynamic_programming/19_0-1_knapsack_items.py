from utils import test_class

# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack.
# Return the maximum value and the weights that were included.
# You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

examples = [
  {
    'input': [50, [60, 100, 120], [10, 20, 30]], # W (knapsack weight), profits, weights
    'output': [220, [30, 20]], # max profit, [weights included]
  },
  {
    'input': [60, [40, 100, 50, 60], [20, 10, 40, 30]],
    'output': [200, [30, 10, 20]],
  },
]

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(n * W)
# Auxiliary Space: O(W)
class Solution:
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

    profit = max_profit[len(weights)][knapsack_weight]
    weight = knapsack_weight

    items = []
    # print(max_profit)
    for pos in range(len(weights) - 1, -1, -1):
      # print(profit, weight, max_profit[pos][weight], weights[pos])
      if profit <= 0: break
      # The result comes from either
      # 1. max_profit[pos][weight], or
      # 2. profits[pos] + max_profit[pos][weight - weights[pos]]
      # If it comes from the first, the weight was not included
      if profit == max_profit[pos][weight]: continue

      items.append(weights[pos])
      profit -= profits[pos]
      weight -= weights[pos]

    return [max_profit[len(weights)][knapsack_weight], items]

test_class(Solution, examples)

from utils import test_class

# Fractional knapsack
# Given the weights and profits of N items in the form of {profit, weight}
# Put these items in a knapsack of capacity W to get the maximum total profit
# In Fractional Knapsack, we can break items for maximizing the total value
# In 0/1 Knapsack, items cannot be broken which is solved using DP

examples = [
  {
    'input': [50, [[60, 10], [100, 20], [120, 30]]], # [Weight, [[profit, weight]]]
    'output': 240
    # Taking items of weights 10 kg, 20 kg, 2/3 of 30 kg, the profit will be 240
  },
  {
    'input': [10, [[500, 30]]],
    'output': 166.667
  },
]

# Naive approach: Try all possible subsets with all different functions
# Time Complexity: O(2^n)
# Auxiliary Space: O(1)

# Greedy approach:
# Calculate the ratio of profit/weight for each item and sort the items based on this ratio
# Take the item with the highest ratio and add them as much as we can
# (can be the whole element or a fraction of it)
# This will always give the maximum profit because in each step it adds an element
# such that this is the maximum possible profit for that much weight
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, knapsack_weight, items):
    # Sort items in descending order by the ration profit/weight
    items.sort(key = lambda item: (item[0] / item[1]), reverse = True)
    total_weight = 0
    total_profit = 0

    for item in items:
      if total_weight + item[1] <= knapsack_weight:
        total_weight += item[1]
        total_profit += item[0]
      else:
        fraction = (knapsack_weight - total_weight) / item[1]
        total_weight += item[1] * fraction
        total_profit += item[0] * fraction
        break

    return round(total_profit, 3)

test_class(Solution, examples)

from utils import test_class

# There are n stairs
# A person standing at the bottom wants to climb stairs to reach the top
# The person can climb either 1 stair or 2 stairs at a time
# Count the number of ways that a person can reach at the top

examples = [
  {
    'input': [1],
    'output': 1
  },
  {
    'input': [2],
    'output': 2
  },
  {
    'input': [4],
    'output': 5
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, stairs):
    if stairs == 0 or stairs == 1: return 1

    # A person can reach the nth stair
    # 1. By taking 1 step from the previous stair
    way1 = self.solve(stairs - 1)
    # 2. By takinng 2 steps from the previous of previous stair
    way2 = self.solve(stairs - 2)
    return way1 + way2

test_class(Solution, examples)

# Memoization (Top-Down)
# If we notice carefully, the above recursive solution holds the two properties of DP
# 1. Optimal Substructure:
# Number of ways to reach the nth stair ways(n) depends on the optimal solutions
# of the subproblems ways(n-1) and ways(n-2).
# By combining these optimal substructures, the total number of ways to reach the nth
# stair can be calculated efficiently.
# 2. Overlapping Subproblems:
# While applying a recursive approach we notice that certain subproblems are computed
# multiple times.
# For example, when calculating ways(4), ways(3) and ways(2) are recursively calculated,
# while ways(3) in turn recursively computes ways(2) again
# This redundancy leads to overlapping subproblems.
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, stairs):
    self.ways = [None] * (stairs + 1)
    return self.count_ways(stairs)

  def count_ways(self, stairs):
    if stairs == 0 or stairs == 1: return 1

    if self.ways[stairs]:
      return self.ways[stairs]

    self.ways[stairs] = self.count_ways(stairs - 1) + self.count_ways(stairs - 2)
    return self.ways[stairs]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution3:
  def solve(self, stairs):
    ways = [0] * (stairs + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, stairs + 1):
      ways[i] = ways[i - 1] + ways[i - 2]

    return ways[stairs]

test_class(Solution3, examples)

# Tabulation (Bottom - Up) with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Similar to Fibonacci

# Matrix Exponentiation
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursion stack
# Similar to Fibonacci

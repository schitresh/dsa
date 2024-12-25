from utils import test_class

# A child is running up a staircase with n steps
# and can hop either 1 step, 2 steps, or 3 steps at a time
# Count the number of possible ways the child can run up the stairs

examples = [
  {
    'input': [4],
    'output': 7,
    # {1, 1, 1, 1}, {1, 2, 1}, {2, 1, 1}, {1, 1, 2}, {2, 2}, {3, 1}, {1, 3}
  },
  {
    'input': [3],
    'output': 4,
    # {1, 1, 1}, {1, 2}, {2, 1}, {3}
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, stairs):
    if stairs < 0: return 0 # For invalid stair
    if stairs == 0: return 1

    # A person can reach the nth stair
    # 1. By jumping 1 stair
    way1 = self.solve(stairs - 1)
    # 2. By jumping 2 stairs
    way2 = self.solve(stairs - 2)
    # 2. By jumping 3 stairs
    way3 = self.solve(stairs - 3)
    return way1 + way2 + way3

test_class(Solution, examples)

# Memoization (Top-Down)
# If we notice carefully, the above recursive solution holds the two properties of DP
# 1. Optimal Substructure:
# Number of ways to reach the nth stair ways(n) depends on the optimal solutions
# of the subproblems ways(n-1), ways(n-2), and ways(n-2).
# By combining these optimal substructures, the total number of ways to reach the nth
# stair can be calculated efficiently.
# 2. Overlapping Subproblems:
# While applying a recursive approach we notice that certain subproblems are computed
# multiple times.
# For example, when calculating ways(4), ways(3), ways(2), and ways(1) are calculated,
# while ways(3) in turn recursively computes ways(2) & ways(1) again
# This redundancy leads to overlapping subproblems.
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, stairs):
    self.ways = [None] * (stairs + 1)
    return self.count_ways(stairs)

  def count_ways(self, stairs):
    if stairs < 0: return 0 # For invalid stair
    if stairs == 0: return 1

    if self.ways[stairs]:
      return self.ways[stairs]

    way1 = self.count_ways(stairs - 1)
    way2 = self.count_ways(stairs - 2)
    way3 = self.count_ways(stairs - 3)
    self.ways[stairs] = way1 + way2 + way3
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
    ways[2] = 2

    for i in range(3, stairs + 1):
      ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[stairs]

test_class(Solution3, examples)

# Tabulation (Bottom - Up) with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, n):
    prev3 = 1
    prev2 = 1
    prev1 = 2

    for _ in range(3, n + 1):
      ways = prev1 + prev2 + prev3
      prev3 = prev2
      prev2 = prev1
      prev1 = ways

    return prev1

test_class(Solution4, examples)

# To do
# Matrix Exponentiation
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursion stack

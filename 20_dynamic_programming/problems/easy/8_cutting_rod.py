from utils import test_class

# Given a rod of length n inches and an array price[], where price[i] denotes the value
# of a piece of length i. Determine the maximum value obtainable by cutting up the rod
# and selling the pieces.

examples = [
  {
    'input': [[1, 5, 8, 9, 10, 17, 17, 20]],
    'output': 22, # Cut into 2 pieces of len 2 & 6 (5 + 17)
  },
  {
    'input': [[3, 5, 8, 9, 10, 17, 17, 20]],
    'output': 24, # Cut into 8 pieces of len 1 (8 * 3)
  },
  {
    'input': [[3]],
    'output': 3,
  },
]

# Recursion
# Time Complexity: O(n^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, prices):
    self.prices = prices
    return self.max_value(len(prices))

  def max_value(self, length):
    if length == 0: return 0

    val = 0
    for piece in range(1, length + 1):
      next_val = self.max_value(length - piece)
      curr_val = self.prices[piece - 1] + next_val
      val = max(val, curr_val)

    return val

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, prices):
    self.prices = prices
    self.memo = [None] * (len(prices) + 1)
    return self.max_value(len(prices))

  def max_value(self, length):
    if length == 0: return 0

    if self.memo[length]:
      return self.memo[length]

    val = 0
    for piece in range(1, length + 1):
      next_val = self.max_value(length - piece)
      curr_val = self.prices[piece - 1] + next_val
      val = max(val, curr_val)

    self.memo[length] = val
    return val

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, prices):
    dp = [None] * (len(prices) + 1)
    dp[0] = 0

    for length in range(1, len(prices) + 1):
      val = 0
      for piece in range(1, length + 1):
        curr_val = prices[piece - 1] + dp[length - piece]
        val = max(val, curr_val)

      dp[length] = val

    return dp[-1]

test_class(Solution3, examples)

# Using Unbounded Knapsack
# This problem is very similar to the unbounded knapsack problem, where there are multiple
# occurrences of the same item. Here we consider length of rod as capacity of knapsack.
# All lengths from 1 to n are considered as weights of items.
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution4:
  def solve(self, prices):
    self.prices = prices
    self.memo = [[None] * (len(prices) + 1) for _ in range(len(prices) + 1)]
    return self.max_value(len(prices), len(prices))

  def max_value(self, piece, length):
    if piece == 0 or length == 0: return 0

    if self.memo[piece][length]:
      return self.memo[piece][length]

    val1 = self.max_value(piece - 1, length)
    val2 = 0
    if piece <= length:
      val2 = self.prices[piece - 1] + self.max_value(piece, length - piece)

    self.memo[piece][length] = max(val1, val2)
    return self.memo[piece][length]

test_class(Solution4, examples)

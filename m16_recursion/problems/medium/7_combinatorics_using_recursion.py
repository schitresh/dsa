from utils import test_class

# Given two numbers n and r, find the value of nCr using recursion.

examples = [
  {
    'input': [5, 2],
    'output': 10,
  },
  {
    'input': [3, 1],
    'output': 3
  },
]

# Naive Approach
# Using the recursion equation: C(n, r) = C(n - 1, r - 1) + C(n - 1, r)
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n, r):
    if n < r: return 0
    if n == 1: return 1
    if r == 0: return 1
    if r == 1: return n

    return self.solve(n - 1, r - 1) + self.solve(n - 1, r)

test_class(Solution, examples)

# Naive Approach
# Using the recursion equation: C(n, r) = C(n, r - 1) * (n - r + 1) / r
# Time Complexity: O(r)
# Auxiliary Space: O(r), due to recursive stack
class Solution2:
  def solve(self, n, r):
    if r == 0: return 1

    return self.solve(n, r - 1) * (n - r + 1) // r

test_class(Solution2, examples)

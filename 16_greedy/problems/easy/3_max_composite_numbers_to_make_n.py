from utils import test_class

# Given n, print the maximum number of composite numbers that sum up to n.
# First few composite numbers are 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, ...

examples = [
  {
    'input': [90],
    'output': 22, # Add 21 of 4 (84) and 1 of 6, so 84 + 6 = 90
  },
  {
    'input': [10],
    'output': 2, # 4 + 6 = 10
  }
]

# Todo
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, num):
    count = 0
    return count

test_class(Solution, examples)

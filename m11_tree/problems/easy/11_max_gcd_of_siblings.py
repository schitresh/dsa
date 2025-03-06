import math
from utils import test_class

# Given a 2d array which represents the nodes of a binary tree, find the maximum GCD of
# the siblings of this tree without actually constructing it.

examples = [
  {
    'input': [[[4, 5], [4, 2], [2, 3], [2, 1], [3, 6], [3, 12]]],
    # [parent, child]
    'output': 6,
    # The siblings with parent 3 has the maximum GCD, i.e. GCD(6, 12) = 6
  },
  {
    'input': [[[5, 4], [5, 8], [4, 6], [4, 9], [8, 10], [10, 20], [10, 30]]],
    'output': 10,
    # The siblings with parent 3 has the maximum GCD, i.e. GCD(6, 12) = 6
  },
  {
    'input': [[[4, 5]]],
    'output': 0,
    # No siblings
  },
]

# Sorting and GCD
# Sort the numbers and calculate gcd for all nodes with the same parent
# Time Complexity: O(n * log(n))
# Space Complexity: O(1)
class Solution:
  def solve(self, array):
    max_gcd = 0
    gcd = 0
    prev_parent = None
    array.sort()

    for edge in array:
      parent, child = edge

      if prev_parent == parent:
        gcd = math.gcd(gcd, child)
      else:
        max_gcd = max(max_gcd, gcd)
        gcd = child

      prev_parent = parent

    return max_gcd

test_class(Solution, examples)

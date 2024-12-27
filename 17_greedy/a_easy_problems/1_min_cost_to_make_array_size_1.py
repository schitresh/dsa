from utils import test_class

# Given an array of n integers, we need to reduce size of array to one. We are allowed
# to select a pair of integers and remove the larger one of these two. This decreases
# the array size by 1. Cost of this operation is equal to value of smaller one. Find out
# minimum sum of costs of operations needed to convert the array into a single element.

examples = [
  {
    'input': [[4, 3, 2]],
    'output': 4,
    # Choose (4, 2) so 4 is removed, then choose (2, 3) so 3 is removed
    # Total cost = 2 + 2 = 4
  },
  {
    'input': [[3, 4]],
    'output': 3
  }
]

# If we always pick the min element, the cost will be low.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    mini = min(array)
    return mini * (len(array) - 1)

test_class(Solution, examples)

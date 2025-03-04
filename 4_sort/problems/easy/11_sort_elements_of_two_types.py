from utils import test_class

# This problem appears in multiple forms:
# Sort a binary array (0s & 1s) with 0s on left side and 1s on right side
# Move all zeros to the end of the array
# Separate even and odd numbers
# Separate negative and positive numbers

# Let's take the last case. Given an array of integers, arrange the elements such that
# all the negative integers appear before all the positive integers in the array.

examples = [
  {
    'input': [[11, -13, 6, -7, 5]],
    'output': [-13, -7, 11, 6, 5],
    # Multiple outputs possible
  },
  {
    'input': [[12, 11, -13, -5, 6, -7, 5, -3, -6]],
    'output': [-13, -5, -7, -3, -6, 12, 11, 6, 5],
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    idx = 0
    pos_idx = 0

    while idx < len(array) and pos_idx < len(array):
      if array[idx] > 0:
        idx += 1
      elif array[pos_idx] < 0:
        pos_idx += 1
      else:
        array[idx], array[pos_idx] = array[pos_idx], array[idx]
        idx += 1
        pos_idx += 1

    return array

test_class(Solution, examples)

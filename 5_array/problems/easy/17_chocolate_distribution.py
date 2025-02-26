from utils import test_class

# Given an array integers where arr[i] represents the number of chocolates in the ith
# packet. Each packet can have a variable number of chocolates. We need to distribute
# chocolates to m students such that:
# - Each student gets exactly one packet.
# - The difference between the maximum and the minimum number of chocolates in the
# packets given to the students is minimized.

examples = [
  {
    'input': [3, [7, 3, 2, 4, 9, 12, 56]],
    'output': 2,
  },
  {
    'input': [5, [7, 3, 2, 4, 9, 12, 56]],
    'output': 7,
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, count, array):
    if len(array) < count: return -1

    array.sort()
    min_diff = float('inf')

    # If count is 3, initial values are min_idx = 0 & max_idx = 2 since both are
    # included in the count
    for max_idx in range(count - 1, len(array)):
      min_idx = max_idx - count + 1
      curr_diff = array[max_idx] - array[min_idx]
      min_diff = min(min_diff, curr_diff)

    return min_diff

test_class(Solution, examples)

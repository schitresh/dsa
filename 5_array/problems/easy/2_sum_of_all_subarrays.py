from utils import test_class

# Given an integer array, find the sum of all sub-arrays of the given array

examples = [
  {
    'input': [[1, 2, 3]],
    'output': 20,
    # [1] + [2] + [3] + [2 + 3] + [1 + 2] + [1 + 2 + 3] = 20
  },
  {
    'input': [[1, 2, 3, 4]],
    'output': 50,
  },
]

# Generate all subarrays
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    result = 0

    for i in range(len(array)):
      curr_sum = 0

      for j in range(i, len(array)):
        curr_sum += array[j]
        result += curr_sum

    return result

test_class(Solution, examples)

# Pattern Formula
# If we take a close look then we observe a pattern.
# For example, [1, 2, 3] has subarrays: [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]
# Here, 1 appears 3 times, 2 appears 4 times, 3 appears 3 times
# Every element appears in two types of subsets:
# 1. In subarrays beginning with the element. There are (n - i) such subsets.
# For example, [2] appears in [2] and [2, 3].
# 2. In subarrays where this element is not the first element. There are (n-i) * i such
# subsets. For example, [2] appears in [1, 2] and [1, 2, 3].
# Hence, total occurences for ith element = (n - i) + (n - i) * i  = (n - i)(i + 1)
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    result = 0

    for i in range(len(array)):
      result += array[i] * (len(array) - i) * (i + 1)

    return result

test_class(Solution2, examples)

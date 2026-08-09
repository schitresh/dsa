from utils import test_class

# Given an array of distinct elements and a range [low, high], find all numbers that
# are in a range, but not the array. The missing elements should be returned in sorted
# order.

examples = [
  {
    'input': [10, 15, [10, 12, 11, 15]],
    'output': [13, 14],
  },
  {
    'input': [50, 55, [1, 14, 11, 51, 15]],
    'output': [50, 52, 53, 54, 55],
  },
  {
    'input': [1, 5, [8, 9, 11, 7, 6]],
    'output': [1, 2, 3, 4, 5],
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
from bisect import bisect_left
class Solution:
  def solve(self, low, high, array):
    missing = []
    array.sort()
    range_num = low

    # Binary search to find low or a larger element in the array
    idx = bisect_left(array, low)
    while idx < len(array) and range_num <= high:
      if array[idx] != range_num:
        missing.append(range_num)
      else:
        idx += 1

      range_num += 1

    while range_num <= high:
      missing.append(range_num)
      range_num += 1

    return missing

test_class(Solution, examples)

# Hashing range nums
# Time Complexity: O(n + high - low)
# Auxiliary Space: O(high - low)
class Solution2:
  def solve(self, low, high, array):
    present = [False] * (high - low + 1)

    for num in array:
      if num < low or num > high: continue
      present[num - low] = True

    missing = []
    for num in range(low, high + 1):
      if not present[num - low]:
        missing.append(num)

    return missing

test_class(Solution2, examples)

# Hashsing array nums
# Time Complexity: O(n + high - low)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, low, high, array):
    present = set(array)
    missing = []

    for num in range(low, high + 1):
      if num not in present:
        missing.append(num)

    return missing

test_class(Solution3, examples)

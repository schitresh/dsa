from bisect import bisect_left # Library for binary search
from utils import test_class

# Given an array of distinct elements and a range [low, high], find all the numbers that
# are in the range but not in the array. The missing elements should be returned in the
# sorted order.

examples = [
  {
    'input': [[10, 12, 11, 15], 10, 15],
    'output': [13, 14],
  },
  {
    'input': [[1, 14, 11, 51, 15], 50, 55],
    'output': [50, 52, 53, 54, 55],
  },
]

# Sorting
# Sort the array and do a binary search for low. Start traversing the array from that
# location and find all missing numbers.
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, low, high):
    missing = []
    array.sort()

    # Do binary search for low in the sorted array and find the index of the first
    # element which is either equal to or greater than low.
    low_index = bisect_left(array, low)

    idx = low_index
    item = low
    while idx < len(array) and item <= high:
      print
      if array[idx] != item: missing.append(item)
      else: idx += 1
      # Move to the next element in the range
      item += 1

    while item <= high:
      missing.append(item)
      item += 1

    return missing

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array, low, high):
    hash_set = set(array)
    missing = []

    for item in range(low, high + 1):
      if item in hash_set: continue
      missing.append(item)

    return missing

test_class(Solution2, examples)

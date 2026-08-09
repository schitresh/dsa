from utils import test_class

# Given an array of integers and a key, find whether the key is present in the array.
# Return the index of the first occurrence  or -1 if it doesn’t exist.

examples = [
  {
    'input': [[4, 5, 6, 7, 8, 9], 8],
    'output': 4
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 4],
    'output': 0
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 2],
    'output': -1
  }
]

# Linear Search
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Comparisons: 2n + 1
# n + 1 comparisons to run the loop (checking that index is not out of bounds)
# n comparisons to compare array items and key
class Solution:
  def solve(self, array, key):
    for i in range(len(array)):
      if array[i] == key:
        return i

    return -1

test_class(Solution, examples)

# Sentinel Linear Search
# Linear search with less comparisons
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Comparisons: n + 2
# n comparisons to compare array items and key
# 2 comparisons after the loop to check if key is found
class Solution2:
  def solve(self, array, key):
    last_i = len(array) - 1
    last_num = array[last_i]
    array[last_i] = key

    i = 0
    while array[i] != key:
      i += 1

    if i < last_i or last_num == key:
      return i

    return -1

test_class(Solution2, examples)

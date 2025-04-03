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

# Ternary Search
# Does more comparisions than binary search
# So binary search is better than ternary search
# Time Complexity: O(2 * log3(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
      mid1 = left + (right - left) // 3
      mid2 = right - (right - left) // 3

      if array[mid1] == key:
        return mid1
      if array[mid2] == key:
        return mid2

      if key < array[mid1]:
        right = mid1 - 1
      elif key < array[mid2]:
        left = mid1 + 1
        right = mid2 - 1
      else:
        left = mid2 + 1

    return -1

test_class(Solution, examples)

# Recursive Ternary Search
# Time Complexity: O(2 * log3(n)), same as iterative
# Auxiliary Space: O(log3(n)) for recusion
class Solution2:
  def solve(self, array, key):
    return self.search(array, key, 0, len(array) - 1)

  def search(self, array, key, left, right):
    if left > right: return - 1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if array[mid1] == key:
      return mid1
    if array[mid2] == key:
      return mid2

    if key < array[mid1]:
      right = mid1 - 1
    elif key < array[mid2]:
      left = mid1 + 1
      right = mid2 - 1
    else:
      left = mid2 + 1

    return self.search(array, key, left, right)

test_class(Solution2, examples)

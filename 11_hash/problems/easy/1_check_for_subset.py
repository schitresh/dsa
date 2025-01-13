from queue import PriorityQueue
from utils import test_class

# Given two arrays a and b of size m and n respectively, determine whether b is a subset
# of a. Both arrays are not sorted, and elements are distinct.

examples = [
  {
    'input': [[11, 1, 13, 21, 3, 7], [11, 3, 7, 1]],
    'output': True,
  },
  {
    'input': [[1, 2, 3, 4, 5, 6], [1, 2, 4]],
    'output': True,
  },
  {
    'input': [[10, 5, 2, 23, 19], [19, 5, 3]],
    'output': False,
  },
]

# Naive Approach
# Check one by one if all the elements of array b are in array a
# Time Complexity: O(m * n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    for item2 in arr2:
      if item2 not in arr1: return False

    return True

test_class(Solution, examples)

# Sorting & Two pointers
# Time Complexity: O(m * log(m) + n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
      # If there is no corresponding matching element in arr1, then it's not a subset
      if arr2[j] < arr1[i]: return False

      if arr2[j] > arr1[i]:
        i += 1
      else:
        i += 1
        j += 1

    return True

test_class(Solution2, examples)

# Hasing
# Time Complexity: O(m + n)
# Auxiliary Space: O(m)
class Solution3:
  def solve(self, arr1, arr2):
    # Python set is a built-in implementation of hash set
    # They are implemented using hash tables, where each element is stored as a key in
    # the table with an associated value of None.
    hash_set = set(arr1)

    for item2 in arr2:
      if item2 not in hash_set: return False

    return True

test_class(Solution3, examples)

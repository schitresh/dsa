from utils import test_class

# Given two arrays, find the intersection (common elements) of the two arrays.
# The intersection should not count the duplicate elements.

examples = [
  {
    'input': [[1, 2, 1, 3, 1], [3, 1, 3, 4, 1]],
    'output': [3, 1],
  },
  {
    'input': [[1, 1, 1], [1, 1, 1, 1, 1]],
    'output': [1],
  },
  {
    'input': [[1, 2, 3], [4, 5, 6]],
    'output': [],
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, arr1, arr2):
    hash_set = set(arr1)
    intersection = []

    for item2 in arr2:
      if item2 in hash_set:
        intersection.append(item2)
        hash_set.remove(item2)

    return intersection

test_class(Solution, examples)

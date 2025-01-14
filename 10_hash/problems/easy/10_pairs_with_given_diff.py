from utils import test_class

# Given an array and a positive integer k, find all the pairs (i, j) such that i < j
# and absolute value of (arr[i] – arr[j]) is equal to k.

examples = [
  {
    'input': [[1, 4, 1, 4, 5], 3],
    'output': [[1, 4], [4, 1], [1, 4], [1, 4]],
  },
  {
    'input': [[8, 16, 12, 16, 4, 0], 4],
    'output': [[8, 12], [16, 12], [12, 16], [8, 4], [4, 0]],
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array, diff):
    pairs = []
    complements = {}

    for item in array:
      target1 = item - diff
      target2 = item + diff

      if target1 in complements:
        for _ in range(complements[target1]):
          pairs.append([target1, item])

      if target2 in complements:
        for _ in range(complements[target2]):
          pairs.append([target2, item])

      complements[item] = complements.get(item, 0) + 1

    return pairs

test_class(Solution, examples)

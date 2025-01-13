from utils import test_class

# Given an array of n integers and a target value, find whether there is a pair of
# elements in the array whose sum is equal to the target.

examples = [
  {
    'input': [[1, 5, 7, -1, 5], 6],
    'output': [[1, 5], [7, -1], [1, 5]],
  },
  {
    'input': [[1, 1, 1, 1], 2],
    'output': [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
  },
  {
    'input': [[10, 12, 10, 15, -1], 125],
    'output': [],
  },
]

# Sorting & Two pointers will not work
# For example, we need to consider all the pairs for example 2

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array, target):
    pairs = []
    complements = {}

    for item in array:
      diff = target - item
      if diff in complements:
        for _ in range(complements[diff]):
          pairs.append([diff, item])

      complements[item] = complements.get(item, 0) + 1

    return pairs

test_class(Solution, examples)

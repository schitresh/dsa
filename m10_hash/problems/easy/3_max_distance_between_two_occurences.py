from utils import test_class

# Given an array find the maximum distance between two occurrences of any element.
# If no element occurs twice, return 0.

examples = [
  {
    'input': [[1, 1, 2, 2, 2, 1]],
    'output': 5,
  },
  {
    'input': [[3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]],
    'output': 10,
  },
  {
    'input': [[1, 2, 3, 6, 5, 4]],
    'output': 0,
  },
]

# Naive Approach
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    max_dist = 0

    for i in range(len(array)):
      for j in range(len(array) - 1, i, -1):
        if array[i] != array[j]: continue
        max_dist = max(max_dist, j - i)

    return max_dist

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    max_dist = 0
    first_index = {}

    for i in range(len(array)):
      if array[i] in first_index:
        max_dist = max(max_dist, i - first_index[array[i]])
      else:
        first_index[array[i]] = i

    return max_dist

test_class(Solution2, examples)

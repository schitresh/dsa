from utils import test_class

# Given an unsorted array that may contain duplicates and a number k (smaller than the
# size of the array), determine if the array contains duplicates within k distance.

examples = [
  {
    'input': [3, [1, 2, 3, 4, 1, 2, 3, 4]],
    'output': False,
  },
  {
    'input': [3, [1, 2, 3, 1, 4, 5]],
    'output': True,
  },
  {
    'input': [3, [1, 2, 3, 4, 5]],
    'output': False,
  },
  {
    'input': [3, [1, 2, 3, 4, 4]],
    'output': True,
  },
]

# Naive Approach
# Time Complexity: O(n * k)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, k, array):
    for i in range(len(array)):
      for j in range(i + 1, len(array) - k):
        if array[i] == array[j]: return True

    return False

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, k, array):
    first_index = {}

    for i in range(len(array)):
      if array[i] in first_index:
        if i - first_index[array[i]] <= k:
          return True
      else:
        first_index[array[i]] = i

    return False

test_class(Solution2, examples)

from utils import test_class

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

# Time Complexity: O(n)
# Space Complexity: O(1)
# Comparisons: 2n + 1
class LinearSearch:
  def solve(self, array, key):
    for i, item in enumerate(array):
      if item == key:
        return i

    return -1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Comparisons: n + 2
# Linear search with less comparisons
class SentinelLinearSearch:
  def solve(self, array, key):
    last_index = len(array) - 1
    last = array[last_index]
    array[last_index] = key

    i = 0
    while array[i] != key:
      i +=1

    if i < last_index or last == key:
      return i

    return -1

test_class(LinearSearch, examples)
test_class(SentinelLinearSearch, examples)

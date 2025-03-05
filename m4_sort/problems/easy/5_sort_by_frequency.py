from functools import cmp_to_key
from utils import test_class

# Sort the elements of an array in the decreasing frequency. If two numbers have the
# same frequency, then keep the one which came first before the other.

examples = [
  {
    'input': [[2, 5, 2, 8, 5, 6, 8, 8]],
    'output': [8, 8, 8, 2, 2, 5, 5, 6],
  },
  {
    'input': [[2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]],
    'output': [8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999],
  },
]

# Hashing & Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    freq = {}

    for i in range(len(array)):
      num = array[i]

      if num in freq:
        freq[num][0] = freq[num][0] + 1
      else:
        freq[num] = [1, i]

    def compare_freq(x, y):
      if freq[x][0] > freq[y][0]: return -1
      if freq[x][0] < freq[y][0]: return 1
      if freq[x][1] < freq[y][1]: return -1
      return 1

    array.sort(key = cmp_to_key(compare_freq))

    return array

test_class(Solution, examples)

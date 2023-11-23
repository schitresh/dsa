from utils import test

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

# Time Complexity: O(log2(log2(n)))
## Worst case: O(n)
# Space Complexity: O(1)
# Better than Binary Search if elements are uniformly distributed
# Meaning that for any index i & j, if (aj - ai) is roughly the similar
# Instead of mid, a value based index is calculated
# Value Index = left + (key - array[left]) * (right - left) / (array[right] - array[left])
# This is derived from the equation of a line `y = mx + c` by putting left & right
class InterpolationSearch:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
      value_index = left + (key - array[left]) * (right - left) // (array[right] - array[left])

      if key < array[value_index]:
        right = value_index - 1
      elif key > array[value_index]:
        left = value_index + 1
      else:
        return value_index

    return -1

test(InterpolationSearch, examples)

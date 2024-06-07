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

# Better than Binary Search if elements are uniformly distributed
  # That is, if for any index i & j, if (aj - ai) is roughly the same
# Instead of mid, a value based index is calculated
  # Value Index = left + (key - array[left]) * (right - left) / (array[right] - array[left])
  # This is derived from the equation of a line `y = mx + c` by putting left & right
# Time Complexity: O(log2(log2(n)))
  # Worst case: O(n)
# Auxiliary Space: O(1)
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

test_class(InterpolationSearch, examples)

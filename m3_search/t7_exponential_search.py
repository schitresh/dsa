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

# Figure out the window exponentially in which the key must be present
# Window indexes: 0 to 2^0, 2^0 to 2^1, 2^1 to 2^2, and so on
# And then binary search the key within that window
# Useful for unbounded arrays with large size
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class ExponentialSearch:
  def solve(self, array, key):
    length = len(array)
    # Important to start with 1 since 0 * 2 will always return 0
    index = 1
    while index < length and array[index] < key:
      index *= 2

    left = index // 2
    right = min(index, length)

    while left <= right:
      # left + right might overflow in some languages
      # So use this expression to calculate mid
      mid = left + (right - left) // 2

      if key < array[mid]:
        right = mid - 1
      elif key > array[mid]:
        left = mid + 1
      else:
        return mid

    return -1

test_class(ExponentialSearch, examples)

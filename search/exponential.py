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

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Useful for unbounded arrays with large size
class ExponentialSearch:
  def solve(self, array, key):
    length = len(array)
    # Important to start with 1 since 0 * 2 will always return 0
    i = 1
    while i < length and array[i] < key:
      i *= 2

    left = i // 2
    right = min(i, length)

    while left <= right:
      # left + right might overflow in some languages, so use this expression to calculate mid
      mid = left + (right - left) // 2

      if key < array[mid]:
        right = mid - 1
      elif key > array[mid]:
        left = mid + 1
      else:
        return mid

    return -1

test(ExponentialSearch, examples)

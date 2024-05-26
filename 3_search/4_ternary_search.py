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

# Time Complexity: O(2 * log3(n))
# Space Complexity: O(1)
# Does more comparisions than binary search, so binary is better than ternary search
class TernarySearch:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
      mid1 = left + (right - left) // 3
      mid2 = right - (right - left) // 3

      if array[mid1] == key:
        return mid1
      if array[mid2] == key:
        return mid2

      if key < array[mid1]:
        right = mid1 - 1
      elif key < array[mid2]:
        left = mid1 + 1
        right = mid2 - 1
      else:
        left = mid2 + 1

    return -1

class RecursiveTernarySearch:
  def search(self, array, key, left, right):
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if array[mid1] == key:
      return mid1
    if array[mid2] == key:
      return mid2

    if key < array[mid1]:
      right = mid1 - 1
    elif key < array[mid2]:
      left = mid1 + 1
      right = mid2 - 1
    else:
      left = mid2 + 1

    return self.search(array, key, left, right)

  def solve(self, array, key):
    return self.search(array, key, 0, len(array) - 1)

test_class(TernarySearch, examples)
test_class(RecursiveTernarySearch, examples)

from utils import test

examples = [
  {
    'input': [[4, 5, 6, 7, 8, 9], 8],
    'output': 4
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 4],
    'output': 0
  }
]

# Time Complexity: O(logn)
# Space Complexity: O(1)
class BinarySearch:
  def solve(self, array, key):
    left = 0
    right = key

    while left < right:
      mid = left + (right - left) // 2

      if key < array[mid]:
        right = mid - 1
      elif key > array[mid]:
        left = mid + 1
      else:
        return mid

    return -1

# Time Complexity: O(logn)
# Space Complexity: O(logn)
class BinarySearchRecursive:
  def search(self, array, key, left, right):
    if left > right:
      return -1

    mid = left + (right - left) // 2

    if key < array[mid]:
      right = mid - 1
    elif key > array[mid]:
      left = mid + 1
    else:
      return mid

    return self.search(array, key, left, right)

  def solve(self, array, key):
    return self.search(array, key, 0, len(array) - 1)

test(BinarySearch, examples)
test(BinarySearchRecursive, examples)

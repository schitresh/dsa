import math
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

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Comparisons: 2 * log(n) excluding the while condition
class BinarySearch:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

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

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Recursion Space: O(log(n))
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

# Time Complexity: O(log(n))
# Space Complexity: O(1)
class MetaBinarySearch:
  def solve(self, array, key):
    length = len(array)
    no_of_bits = int(math.log2(length - 1)) + 1

    index = 0
    # Decrement (no of bits - 1) because the bit multiplier for 1st position is 0 (2^0)
    for shift in range(no_of_bits - 1, -1, -1):
      if array[index] == key:
        return index

      new_index = index + 1 << shift
      # OR new_index = index | (1 << shift)

      if new_index < length and array[new_index] <= key:
        index = new_index

    return index if array[index] == key else -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Comparisons: log(n) + 2 excluding the while condition
# Less comparisons than regular binary search
class UbiquitousBinarySearch:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

    while left + 1 < right:
      mid = left + (right - left) // 2

      if key < array[mid]:
        right = mid
      else:
        left = mid

    if array[left] == key:
      return left
    if array[right] == key:
      return right
    return -1

test_class(BinarySearch, examples)
test_class(BinarySearchRecursive, examples)
test_class(MetaBinarySearch, examples)
test_class(UbiquitousBinarySearch, examples)

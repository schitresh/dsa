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
# Auxiliary Space: O(1)
# Comparisons: 2 * log(n) excluding the while condition
class BinarySearch:
  def solve(self, array, key):
    left = 0
    right = len(array) - 1

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

# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)) for recursion
class RecursiveBinarySearch:
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

# Works by constructing the index (that holds the key) in binary
# Avoids overflow errors, but slower than regular binary search
# Also called one sided binary search
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class MetaBinarySearch:
  def solve(self, array, key):
    length = len(array)
    # Number of bits required to represent the largest index (length - 1)
    # Since log2 can return decimal, convert it to integer and add 1 (or use ceiling function)
    # If the length is 7, 3 bits are required to represent the highest index 6
    no_of_bits = int(math.log2(length - 1)) + 1

    index = 0
    if index < length and array[index] == key:
      return index

    # Contruct the binary index from left to right, i.e. most significant bit first
    # If no_of_bits is 3, the first iteration will be to select 1-- or 0--
    # If the key is less than the element, select 0-- else select 1--
    # If 1-- is selected, the second iteration will be to select 11- or 10-
    for shift in range(no_of_bits - 1, -1, -1):
      # New index depending on whether it was selected as index or not in last iteration (for no_of_bits = 3)
      # First iteration: 4
      # Second iteration: 2 or 6
      # Third iteration: 1 or 3 or 5 or 7
      new_index = index + (1 << shift) # Equivalent to index + (1 * 2^shift)

      if new_index > length:
        continue

      if array[new_index] == key:
        return new_index

      if array[new_index] < key:
        index = new_index

    return -1

# Less comparisons than the regular binary search
# This happens because the equality condition is not checked within the loop
# It is checked only once after the loop
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
# Comparisons: log(n) + 2 excluding the while condition
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
test_class(RecursiveBinarySearch, examples)
test_class(MetaBinarySearch, examples)
test_class(UbiquitousBinarySearch, examples)

from utils import test_class

# Given an array of integers and a target value, find whether there is a pair of
# elements in the array whose sum is equal to the target.

examples = [
  {
    'input': [[0, -1, 2, -3, 1], -2],
    'output': [-3, 1],
  },
  {
    'input': [[1, -2, 1, 0, 5], 0],
    'output': None,
  },
]

# Generate all pairs
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

# Sorting with binary search
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, target):
    array.sort()

    for i in range(len(array)):
      complement = target - array[i]
      index = self.binary_search(array, complement, i + 1, len(array) - 1)
      if index: return [array[i], array[index]]

    return None

  def binary_search(self, array, key, left, right):
    while left <= right:
      mid = left + (right - left) // 2

      if array[mid] < key:
        left = mid + 1
      elif array[mid] > key:
        right = mid - 1
      else:
        return mid

    return None

test_class(Solution, examples)

# Sorting with two pointers
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array, target):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
      pair_sum = array[left] + array[right]

      if pair_sum < target:
        left += 1
      elif pair_sum > target:
        right -= 1
      else:
        return [array[left], array[right]]

    return None

test_class(Solution2, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, array, target):
    # Can use set() as well, since we just need to track if complement is present or not
    complements = {}

    for num in array:
      complement = target - num
      if complements.get(complement):
        return [complement, num]

      complements[num] = True

    return None

test_class(Solution3, examples)

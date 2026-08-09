from utils import test_class

# Right Rotation
# Rotate a given array by k places in right/clockwise direction

examples = [
  {
    'input': [[1, 2, 3, 4, 5], 2],
    'output': [4, 5, 1, 2, 3]
  },
  {
    'input': [[1, 2, 3, 4, 5], 8],
    'output': [3, 4, 5, 1, 2]
  },
  {
    'input': [[1, 2, 3, 4, 5], 5],
    'output': [1, 2, 3, 4, 5]
  }
]

# Rotate one by one
# By rotating items by one place for rotate_by number of times
# Time Complexity: O(n * rotate_by)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, rotate_by):
    rotate_by = rotate_by % len(array)

    for _ in range(rotate_by):
      self.rotate_by_one(array)

    return array

  def rotate_by_one(self, array):
    last_index = len(array) - 1
    last_item = array[last_index]

    # For left rotation, iterate from left to right
    for i in range(last_index, 0, -1):
      array[i] = array[i - 1]

    array[0] = last_item

test_class(Solution, examples)

# Using temp array
# Find the rotated place of an element and store it in another array
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array, rotate_by):
    rotate_by = rotate_by % len(array)
    output = [0] * len(array)

    for i in range(len(array)):
      rotated_index = (i + rotate_by) % len(array)
      output[rotated_index] = array[i]

    return output

test_class(Solution2, examples)

# Juggling Algorithm
# Each cycle of rotation is independent and represents a group of elements that will
# shift among themselves during the rotation. If the starting index of a cycle is i,
# then it will be shifted to (i + d) % n, the element at that place will be shifted to
# (i + 2d) % n and so on till we reach back to index i.
# Divide the array into different sets of these cycles. The number of sets is equal to
# GCD of array length & rotate_by. Rotate elements among these sets for each position
# of the first set.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array, rotate_by):
    rotate_by = rotate_by % len(array)
    size_of_set = self.gcd(len(array), rotate_by)

    for pos in range(size_of_set):
      temp = array[pos]
      index = pos
      # For left rotation, do (index + rotate_by) % n
      next_index = (index - rotate_by) % len(array)

      while next_index != pos:
        array[index] = array[next_index]
        index = next_index
        next_index = (index - rotate_by) % len(array)

      array[index] = temp

    return array

  def gcd(self, a, b):
    if b == 0: return a
    return self.gcd(b, a % b)

test_class(Solution3, examples)

# Reversal Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, array, rotate_by):
    rotate_by = rotate_by % len(array)

    # 5, 4, 3, 2, 1
    self.reverse(array, 0, len(array) - 1)
    # 4, 5, 3, 2, 1
    self.reverse(array, 0, rotate_by - 1)
    # 4, 5, 1, 2, 3
    self.reverse(array, rotate_by, len(array) - 1)

    return array

  # In-built methods will copy the array & increase space complexity
  def reverse(self, array, left, right):
    while left < right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1

test_class(Solution4, examples)

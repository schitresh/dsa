from utils import test_class

# Right Rotation
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

# Rotate items one by one, by iterating rotate_by number of times
# Time Complexity: O(n * rotate_by)
# Auxiliary Space: O(1)
class RotateOneByOne:
  def rotate_by_one(self, array):
    last_index = len(array) - 1
    last_item = array[last_index]

    # For left rotation, iterate from left to right
    for i in range(last_index, 0, -1):
      array[i] = array[i - 1]

    array[0] = last_item

  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)

    for _ in range(rotate_by):
      self.rotate_by_one(array)

    return array

# Find the rotated place of an element and store it in another array
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class RotateUsingTempArray:
  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)
    output = [0] * len(array)

    for i in range(len(array)):
      rotated_index = (i + rotate_by) % len(array)
      output[rotated_index] = array[i]

    return output

# Divide the array into different sets
# The number of sets is equal to GCD of array length & rotate_by
# Rotate elements among these sets for each position of the first set
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class RotateByJuggling:
  def gcd(self, a, b):
    if b == 0:
      return a

    return self.gcd(b, a % b)

  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)
    size_of_set = self.gcd(len(array), rotate_by)

    for pos in range(size_of_set):
      temp = array[pos]
      index = pos
      # For left rotation, do index + rotate_by
      next_index = (index - rotate_by) % len(array)

      while next_index != pos:
        array[index] = array[next_index]
        index = next_index
        next_index = (index - rotate_by) % len(array)

      array[index] = temp

    return array

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class RotateByReversal:
  # In-built methods will copy the array & increase space complexity
  def reverse(self, array, left, right):
    while left < right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1

  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)

    # 5, 4, 3, 2, 1
    self.reverse(array, 0, len(array) - 1)
    # 4, 5, 3, 2, 1
    self.reverse(array, 0, rotate_by - 1)
    # 4, 5, 1, 2, 3
    self.reverse(array, rotate_by, len(array) - 1)

    return array

test_class(RotateOneByOne, examples)
test_class(RotateUsingTempArray, examples)
test_class(RotateByJuggling, examples)
test_class(RotateByReversal, examples)

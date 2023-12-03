from utils import test

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

# Time Complexity: O(n * rotate_by)
# Space Complexity: O(1)
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

# Time Complexity: O(n)
# Space Complexity: O(n)
class RotateUsingTempArray:
  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)
    output = [0] * len(array)

    for i in range(len(array)):
      rotated_index = (i + rotate_by) % len(array)
      output[rotated_index] = array[i]

    return output

class RotateByJuggling:
  def gcd(self, a, b):
    if b == 0:
      return a

    return self.gcd(b, a % b)

  def solve(self, array, rotate_by):
    array = array.copy()
    rotate_by = rotate_by % len(array)
    gcd = self.gcd(len(array), rotate_by)

    for i in range(gcd):
      j = i
      # For left rotation, do j + rotate_by
      k = (j - rotate_by) % len(array)
      temp = array[j]

      while k != i:
        array[j] = array[k]
        j = k
        k = (j - rotate_by) % len(array)

      array[j] = temp

    return array

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

test(RotateOneByOne, examples)
test(RotateUsingTempArray, examples)
test(RotateByJuggling, examples)
test(RotateByReversal, examples)

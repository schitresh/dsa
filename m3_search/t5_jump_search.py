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
    'input': [[4, 5, 6, 7, 8, 9], 9],
    'output': 5
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 2],
    'output': -1
  },
  {
    'input': [[4], 4],
    'output': 0
  }
]

# Divide the array into windows of fixed size
# Find the window where key must be present, and then linear search within it
# Time Complexity: O(sqrt(n))
  # Linear < Jump < Binary
# Auxiliary Space: O(1)
# Comparisons: (length/step) + (step - 1)
  # Comparisons will be least when step is sqrt(length)
class JumpSearch:
  def solve(self, array, key):
    length = len(array)
    # Subtract 1 because sqrt of 1 is 1 which will be out of bounds
    step = int(math.sqrt(length)) - 1
    left = 0
    right = step

    # Iterate the windows (bounded by left & right)
    # And find the window where the key must be present
    while array[right] < key:
      left = right
      right += step
      if right >= length:
        return -1

    # Linear search within the selected window
    for i in range(left, right + 1):
      if array[i] == key:
        return i

    return -1

test_class(JumpSearch, examples)

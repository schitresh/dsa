import math
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

# Time Complexity: O(sqrt(n))
## Linear < Jump < Binary
# Space Complexity: O(1)
# Comparisons: (length/step) + (step - 1)
## Comparisons will be least when step is sqrt(length)
class JumpSearch:
  def solve(self, array, key):
    length = len(array)
    step = int(math.sqrt(length))
    left = 0
    right = step

    while array[right] < key:
      left = right
      right += step
      if right >= length:
        return -1

    for i in range(left, right + 1):
      if array[i] == key:
        return i

    return -1

test(JumpSearch, examples)

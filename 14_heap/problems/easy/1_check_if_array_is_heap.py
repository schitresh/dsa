from utils import test_class

# Check if the given array represents a binary max heap.

examples = [
  {
    'input': [[90, 15, 10, 7, 12, 2]],
    'output': True,
  },
  {
    'input': [[9, 15, 10, 7, 12, 11]],
    'output': False,
  },
]

# Recursion
# Continuously check that left & right elements are smaller than the parent node
# Time Complexity: O(n)
# Auxiliary Space: O(h), due to recursive stack (h is height of the tree)
class Solution:
  def solve(self, array):
    self.array = array

    return self.check_descendants(0)

  def check_descendants(self, index):
    left = 2 * index + 1
    right = left + 1

    if left < len(self.array):
      if self.array[left] > self.array[index]: return False
      if not self.check_descendants(left): return False

    if right < len(self.array):
      if self.array[right] > self.array[index]: return False
      if not self.check_descendants(right): return False

    return True

test_class(Solution, examples)

# Iteration
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    last_parent = len(array) // 2 - 1

    for index in range(last_parent + 1):
      left = 2 * index + 1
      right = left + 1

      if array[left] > array[index]: return False
      if right < len(array):
        if array[right] > array[index]: return False

    return True

test_class(Solution2, examples)

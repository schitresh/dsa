from utils import test_class

# convert the given decimal number into an equivalent binary number.

examples = [
  {
    'input': [[1, 8, 9]],
    'output': 18
  },
  {
    'input': [[2, 55, 1, 7]],
    'output': 65
  },
]

# Non-Tail Recursion
# Time Complexity: O(log2(n))
# Auxiliary Space: O(log2(n)), due to recursive stack
class Solution:
  def solve(self, array):
    self.array = array
    return self.sum_array(len(array) - 1)

  def sum_array(self, index):
    if index == -1: return 0
    return self.array[index] + self.sum_array(index - 1)

test_class(Solution, examples)

# Tail Recursion
# Time Complexity: O(log2(n))
# Auxiliary Space: O(log2(n)), due to recursive stack
class Solution2:
  def solve(self, array):
    self.array = array
    return self.sum_array(len(array) - 1, 0)

  def sum_array(self, index, sum):
    if index == -1: return sum

    new_sum = sum + self.array[index]
    return self.sum_array(index - 1, new_sum)

test_class(Solution2, examples)

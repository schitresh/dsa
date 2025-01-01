from utils import test_class

# Find the mean of the elements of given array

examples = [
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': 3
  },
]

# To find the mean using recursion, assume that the problem is already solved for N-1
# Sum of first N-1 elements = (Mean of N-1 elements) * (N-1)
# Mean of N elements = (Sum of first N-1 elements + Nth element) / N
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, array):
    self.array = array
    return self.mean(len(array) - 1)

  def mean(self, index):
    if index == -1: return 0

    sum_rest = self.mean(index - 1) * index
    sum_curr = self.array[index] + sum_rest
    return sum_curr / (index + 1)

test_class(Solution, examples)

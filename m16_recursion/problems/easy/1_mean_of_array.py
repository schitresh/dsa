from utils import test_class

# Find the mean of the numbers in a given array

examples = [
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': 3
  },
]

# Recursion
# Assume that the problem is already solved for n - 1
# sum(n - 1) = mean(n - 1) * (n - 1)
# mean(n) = (sum(n - 1) + arr[n]) / n
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

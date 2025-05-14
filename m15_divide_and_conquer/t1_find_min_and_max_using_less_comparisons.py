from utils import test_class

# Find the maximum and the minimum element of the given array using minimum number
# of comparisons

examples = [
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': [1, 5],
  },
  {
    'input': [[5, 6, 3, 2, 1, 4]],
    'output': [1, 6],
  }
]

# Linear Search
# Find min and max individually by comparing each element
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Comparisions: 2 * (n - 1)

# Tournament Method
# Instead of comparing every element against the current minimum and maximum separately:
# 1. The elements are compared in pairs to track both min and max together, that takes
# take n/2 comparisons.
# 2. The winners of min comparisons are compared with each other to find the final min,
# that takes n/2 - 1 comparisons. The same is done for max comparisons.
# Hence, the total number of comparisons is n/2 + 2 * (n/2 - 1) = 3/2 * n - 2
# Time Complexity: O(n)
# Auxiliary Space: O(log(n)), due to recursive stack
# Comparisons: 3/2 * n - 2
class Solution:
  def solve(self, array):
    return self.find_max_and_min(array, 0, len(array) - 1)

  def find_max_and_min(self, array, left, right):
    if left == right:
      return [array[left], array[right]]

    if left + 1 == right:
      if array[left] < array[right]:
        return [array[left], array[right]]
      else:
        return [array[right], array[left]]

    mid = left + (right - left) // 2
    left_min, left_max = self.find_max_and_min(array, left, mid)
    right_min, right_max = self.find_max_and_min(array, mid + 1, right)

    return [min(left_min, right_min), max(left_max, right_max)]

test_class(Solution, examples)

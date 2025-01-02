from utils import test_class

# Given a set[] of non-negative integers and a value sum, print the subset of the given
# set whose sum is equal to the given sum.

examples = [
  {
    'input': [3, [1, 2, 1]],
    'output': [[1, 2], [2, 1]]
  },
  {
    'input': [30, [3, 34, 4, 12, 5, 2]],
    'output': []
  },
]

# Backtracking
# Subset sum can also be thought of as a special case of the 0-1 Knapsack problem.
# For each item, there are two possibilities:
# 1. Include the current element in the subset and recur for the remaining elements with
# the remaining sum.
# 2. Exclude the current element from the subset and recur for the remaining elements.
# The recursion’s base case would be when no items are left or the sum becomes negative.
# Finally, if sum becomes 0 then include current subset.
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, req_sum, array):
    self.req_sum = req_sum
    self.array = array
    self.subsets = []
    self.check_sum(0, [], 0)
    return self.subsets

  def check_sum(self, index, subset, current_sum):
    if current_sum == self.req_sum:
      self.subsets.append(subset)
      return

    if current_sum > self.req_sum or index == len(self.array):
      return

    element = self.array[index]
    # Considering the current element
    self.check_sum(index + 1, subset + [element], current_sum + element)
    # Without considering the current element (Backtracking)
    self.check_sum(index + 1, subset, current_sum)

test_class(Solution, examples)

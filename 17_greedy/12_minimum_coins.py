from utils import test_class

# Given a value of V Rs and an infinite supply of each of the denominations
# {1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes
# The task is to find the minimum number of coins and/or notes needed to make the change

examples = [
  {
    'input': [70],
    'output': [50, 20]
  },
  {
    'input': [121],
    'output': [100, 20, 1]
  },
  {
    'input': [93],
    'output': [50, 20, 20, 2, 1]
  },
]

# Greedy approach: Start with the largest possible denomination and keep adding
# But this may not work for all denominations, like [9, 6, 5, 1] and V = 11
# This would print 9, 1, 1, but we can use 2 denominations 5 & 6
# For general input, dynamic programming needs to be used
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, value):
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    curr_value = 0
    change = []

    i = len(denominations) - 1
    while i >= 0:
      rem_value = value - curr_value
      if rem_value >= denominations[i]:
        curr_value += denominations[i]
        change.append(denominations[i])
      else:
        i -= 1

    return change

test_class(Solution, examples)

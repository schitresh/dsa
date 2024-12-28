from utils import test_class

# Given an array of non-negative integers and a value sum, check if there is a subset
# of the given array whose sum is equal to the given sum.

examples = [
  {
    'input': [9, [3, 34, 4, 12, 5, 2]],
    'output': True, # [4, 5]
  },
  {
    'input': [30, [3, 34, 4, 12, 5, 2]],
    'output': False
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, sub_sum, array):
    self.array = array
    return self.subset_sum(0, sub_sum)

  def subset_sum(self, index, rem_sum):
    if rem_sum == 0: return True
    if rem_sum < 0: return False
    if index == len(self.array): return False

    path1 = self.subset_sum(index + 1, rem_sum - self.array[index])
    if path1: return True

    return self.subset_sum(index + 1, rem_sum)

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n * sum)
# Auxiliary Space: O(n * sum)
class Solution2:
  def solve(self, sub_sum, array):
    self.array = array
    self.memo = [[None] * (sub_sum + 1) for _ in range(len(array))]
    return self.subset_sum(0, sub_sum)

  def subset_sum(self, index, rem_sum):
    if rem_sum == 0: return True
    if rem_sum < 0: return False
    if index == len(self.array): return False

    if self.memo[index][rem_sum] is not None:
      return self.memo[index][rem_sum]

    path1 = self.subset_sum(index + 1, rem_sum - self.array[index])
    if path1:
      self.memo[index][rem_sum] = True
      return True

    self.memo[index][rem_sum] = self.subset_sum(index + 1, rem_sum)
    return self.memo[index][rem_sum]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, sub_sum, array):
    dp = [[False] * (sub_sum + 1) for _ in range(len(array) + 1)]

    # If sum is 0, then answer will always be true
    for index in range(len(array) + 1):
      dp[index][0] = True

    for index in range(len(array)):
      for curr_sum in range(1, sub_sum + 1):
        sum1 = curr_sum
        path1 = dp[index][sum1]

        sum2 = curr_sum - array[index]
        path2 = False
        if sum2 >= 0:
          path2 = dp[index][sum2]

        dp[index + 1][curr_sum] = path1 or path2

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, sub_sum, array):
    prev = [False] * (sub_sum + 1)
    prev[0] = True

    for index in range(len(array)):
      curr = [False] * (sub_sum + 1)

      for curr_sum in range(sub_sum + 1):
        sum1 = curr_sum
        path1 = prev[sum1]

        sum2 = curr_sum - array[index]
        path2 = False
        if sum2 >= 0:
          path2 = prev[sum2]

        curr[curr_sum] = path1 or path2

      prev = curr

    return prev[-1]

test_class(Solution4, examples)

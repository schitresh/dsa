from utils import test_class

# Given an array, an inversion is defined as a pair a[i], a[j] such that i < j and
# a[i] > a[j]. We are given two numbers n and k, the task is to find how many permutations
# of the first n number have exactly k inversion.

examples = [
  {
    'input': [3, 1], # num, inversion
    'output': 2,
    # Permutations of first 3 numbers: 123, 132, 213, 231, 312, 321
    # Permutations with 1 inversion: 132, 213
  },
  {
    'input': [3, 3],
    'output': 1,
    # 321
  },
  {
    'input': [4, 3],
    'output': 6,
    # 4123, 4132, 4213, 4231, 4312, 4321
  },
]

# Naive Recursion
# Time Complexity: O(n! * k)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n, inversion):
    self.inversion = inversion
    num = list(range(1, n + 1))
    return self.permutations(num, 0)

  def permutations(self, num, index):
    if index == len(num) - 1:
      if self.inv_count(num) == self.inversion: return 1
      return 0

    count = 0
    for j in range(index, len(num)):
      new_num = num.copy()
      new_num[index], new_num[j] = new_num[j], new_num[index]

      count += self.permutations(new_num, index + 1)

    return count

  def inv_count(self, num):
    inversion = 0

    for i in range(len(num)):
      for j in range(i + 1, len(num)):
        if num[i] > num[j]: inversion += 1

    return inversion

test_class(Solution, examples)

# Todo: Understand the recursion formula
# Recursion
# Time Complexity: O(n! * k)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, n, inversion):
    if n == 0: return 0
    # Only one way to have 0 inversions, i.e. sorted order
    if inversion == 0: return 1

    count = 0
    for i in range(min(n - 1, inversion) + 1):
      count += self.solve(n - 1, inversion - i)

    return count

test_class(Solution2, examples)

# Memoization
# Time Complexity: O(n * k * k)
# Auxiliary Space: O(n * k)
class Solution3:
  def solve(self, n, inversion):
    self.memo = [[None] * (inversion + 1) for _ in range(n + 1)]
    return self.permutations(n, inversion)

  def permutations(self, n, inversion):
    if n == 0: return 0
    # Only one way to have 0 inversions, i.e. sorted order
    if inversion == 0: return 1

    if self.memo[n][inversion]:
      return self.memo[n][inversion]

    count = 0
    for i in range(min(n - 1, inversion) + 1):
      count += self.permutations(n - 1, inversion - i)

    self.memo[n][inversion] = count
    return count

test_class(Solution3, examples)

# Tabulation
# Time Complexity: O(n * k * k)
# Auxiliary Space: O(n * k)
class Solution4:
  def solve(self, n, inversion):
    dp = [[0] * (inversion + 1) for _ in range(n + 1)]

    for i in range(n + 1):
      dp[i][0] = 1

    for i in range(1, n + 1):
      for j in range(1, inversion + 1):
        for k in range(min(i - 1, j) + 1):
          dp[i][j] += dp[i - 1][j - k]

    return dp[-1][-1]

test_class(Solution4, examples)

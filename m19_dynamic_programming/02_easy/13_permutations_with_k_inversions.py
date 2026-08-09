from utils import test_class

# Given an array, an inversion is defined as a pair (a[i], a[j]) such that i < j and
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

# Recursion Relation
# Consider we need to count inversions for n = 4, i.e. the numbers are 1, 2, 3, 4.
# Let's say we have counted inversions for n = 3, then place 4 at the following
# permutations:
# 1. At the end: then the new inversions for 4 are 0 because all number before 4
# (i.e. 1, 2, 3) will be smaller irrespective of how they are arranged. That means
# we need to find permutations for n = 3 with k inversions.
# Hence, with 4 at index 2, inv(4, k) = inv(3, k)
# 2. Second position from the end: then the new inversions for 4 are 1 because
# any number put after 4 will be smaller. E.g. 1243, 1342, 2341, etc.
# This means we need to find permuations for n = 3 with (k - 1) inversions.
# Hence, with 4 at index 2, inv(4, k) = inv(3, k - 1)
# And so on.

# Thus, inv(4, k) = inv(i = 3)(3, k) + inv(i = 2)(3, k - 1) + inv(i = 1)(3, k - 2)
#                   + inv(i = 0)(3, k - 3)
# Though we need to avoid i = 0 if k = 2.
# So the recurrence relation is:
# inv(n, k) = Sum[i = 0 to min(n - 1, k)] { inv(n - 1, k - i) }
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

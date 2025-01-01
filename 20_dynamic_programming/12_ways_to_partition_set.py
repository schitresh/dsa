from utils import test_class

# Given a set of n elements, find the number of ways of partitioning it.

# Bell Number
# Let S(n, k) be total number of partitions of n elements into k sets.
# The value of the nth Bell Number is the sum of S(n, k) for k = 1 to n.
# Bell(n) = Sum(k = 1 to n)[S(n, k)]
# Value of S(n, k) can be defined recursively as: S(n + 1, k) = k * S(n, k) + S(n, k - 1)
# How does above recursive formula work?
# When we add a (n + 1)th element to k partitions, there are two possibilities.
# 1) It is added as a single element set to existing partitions, i.e, S(n, k - 1)
# 2) It is added to all sets of every partition, i.e., k * S(n, k).
# First few Bell numbers are 1, 1, 2, 5, 15, 52, 203, ...

examples = [
  {
    'input': [2],
    'output': 2,
    # Let the set be [1, 2], partitions are: [[1], [2]], [[1, 2]]
  },
  {
    'input': [3],
    'output': 5,
    # Let the set be [1, 2, 3], partitions are:
    # [[1], [2], [3]], [[1], [2, 3]], [[2], [1, 3]], [[3], [1, 2]], [[1, 2, 3]]
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, num):
    bell_number = 0

    # Sum up stirling numbers S(n, k) for all k from 1 to n
    for k in range(1, num + 1):
      bell_number += self.stirling(num, k)

    return bell_number

  def stirling(self, num, k):
    if num == 0 and k == 0: return 1
    if num == 0 or k == 0: return 0
    if num == k: return 1
    if k == 1: return 1

    return k * self.stirling(num - 1, k) + self.stirling(num - 1, k - 1)

test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, num):
    bell_number = 0
    self.memo = [[None] * (num + 1) for _ in range(num + 1)]

    # Sum up stirling numbers S(n, k) for all k from 1 to n
    for k in range(1, num + 1):
      bell_number += self.stirling(num, k)

    return bell_number

  def stirling(self, num, k):
    if num == 0 and k == 0: return 1
    if num == 0 or k == 0: return 0
    if num == k: return 1
    if k == 1: return 1

    if self.memo[num][k]:
      return self.memo[num][k]

    self.memo[num][k] = k * self.stirling(num - 1, k) + self.stirling(num - 1, k - 1)
    return self.memo[num][k]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution3:
  def solve(self, num):
    dp = [[0] * (num + 1) for _ in range(num + 1)]

    for i in range(num + 1):
      for j in range(num + 1):
        if j > i:
          dp[i][j] = 0
        elif i == j:
          dp[i][j] = 1
        elif i == 0 or j == 0:
          dp[i][j] = 0
        else:
          dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]

    bell_number = 0
    for i in range(num + 1):
      bell_number += dp[num][i]

    return bell_number

test_class(Solution3, examples)

# Tabulation (Bottom-Up)
# Using bell triangle: [[1], [1, 2], [2, 3, 5], [5, 7, 10, 15]]
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution4:
  def solve(self, num):
    dp = [[0] * (num + 1) for _ in range(num + 1)]
    dp[0][0] = 1

    for i in range(1, num + 1):
      dp[i][0] = dp[i - 1][i - 1]

      for j in range(1, num + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    return dp[num][0]

test_class(Solution4, examples)

# Tabulation (Bottom-Up) with space optimization
# Store last row of bell triangle: [[1], [1, 2], [2, 3, 5], [5, 7, 10, 15]]
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution5:
  def solve(self, num):
    dp = [0] * (num + 1)
    dp[0] = 1

    for i in range(1, num + 1):
      prev = dp[0]
      dp[0] = dp[i - 1]

      for j in range(1, num + 1):
        temp  = dp[j]
        dp[j] = prev + dp[j - 1]
        prev = temp

    return dp[0]

test_class(Solution5, examples)

from utils import test_class

# Given an integer values n and k, find the value of Binomial Coefficient C(n, k).
# A binomial coefficient C(n, k) can be defined as the coefficient of x^k
# in the expansion of (1 + x)^n.
# A binomial coefficient C(n, k) also gives the number of ways, disregarding order,
# that k objects can be chosen from among n objects. More formally, the number of
# k-element subsets (or k-combinations) of a n-element set.

examples = [
  {
    'input': [4, 2],
    'output': 6,
  },
  {
    'input': [5, 2],
    'output': 10,
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, n, k):
    if k > n: return 0
    if k == 0 or k == n: return 1

    return self.solve(n - 1, k - 1) + self.solve(n - 1, k)

test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(n * k)
# Auxiliary Space: O(n * k)
class Solution2:
  def solve(self, n, k):
    self.memo = [[None] * (k + 1) for _ in range(n + 1)]
    return self.binomial_coeff(n, k)

  def binomial_coeff(self, n, k):
    if k > n: return 0
    if k == 0 or k == n: return 1

    if self.memo[n][k]:
      return self.memo[n][k]

    self.memo[n][k] = self.binomial_coeff(n - 1, k - 1) + self.binomial_coeff(n - 1, k)
    return self.memo[n][k]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n * k)
# Auxiliary Space: O(n * k)
class Solution3:
  def solve(self, n, k):
    dp = [[None] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
      for j in range(min(i, k) + 1):
        if j == 0 or j == i:
          dp[i][j] = 1
        else:
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

test_class(Solution3, examples)

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution4:
  def solve(self, n, k):
    dp = [0] * (k + 1)
    dp[0] = 1 # nC0 is 1

    for i in range(1, n + 1):
      for j in range(min(i, k), 0, -1):
        dp[j] = dp[j] + dp[j - 1]

    return dp[k]

test_class(Solution4, examples)

from utils import test_class

# Given two strings s1 and s2, find the length of the Longest Common Subsequence.
# If there is no common subsequence, return 0.
# A subsequence is a string generated from the original string by deleting 0 or more
# characters and without changing the relative order of the remaining characters.
# For example, subsequences of ABC are '', A, B, C, AB, AC, BC and ABC.
# In general, a string of length n has 2n subsequences.

examples = [
  {
    'input': ['abc', 'acd'],
    'output': 2, # The longest subsequence present in both strings is 'ac'
  },
  {
    'input': ['aggtab', 'gxtxayb'],
    'output': 4, # LCS is 'gtab'
  },
  {
    'input': ['abc', 'cba'],
    'output': 1, # LCS are 'a', 'b', 'c'
  },
    {
    'input': ['abdefc', 'ac'],
    'output': 2, # LCS is 'ac'
  },
]

# Recursion
# Time Complexity: O(2^min(m, n))
# Auxiliary Space: O(min(m, n))
class Solution:
  def solve(self, string1, string2):
    return self.lcs(string1, len(string1) - 1, string2, len(string2) - 1)

  def lcs(self, sub1, index1, sub2, index2):
    if index1 < 0 or index2 < 0: return 0

    if sub1[index1] == sub2[index2]:
      return 1 + self.lcs(sub1, index1 - 1, sub2, index2 - 1)

    len1 = self.lcs(sub1, index1 - 1, sub2, index2)
    len2 = self.lcs(sub1, index1, sub2, index2 - 1)
    return max(len1, len2)

test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution2:
  def solve(self, string1, string2):
    self.memo = [[None] * len(string2) for _ in range(len(string1))]
    return self.lcs(string1, len(string1) - 1, string2, len(string2) - 1)

  def lcs(self, sub1, index1, sub2, index2):
    if index1 < 0 or index2 < 0: return 0

    if self.memo[index1][index2]:
      return self.memo[index1][index2]

    if sub1[index1] == sub2[index2]:
      self.memo[index1][index2] = 1 + self.lcs(sub1, index1 - 1, sub2, index2 - 1)
      return self.memo[index1][index2]

    len1 = self.lcs(sub1, index1 - 1, sub2, index2)
    len2 = self.lcs(sub1, index1, sub2, index2 - 1)
    self.memo[index1][index2] = max(len1, len2)
    return self.memo[index1][index2]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution3:
  def solve(self, string1, string2):
    # Track length in the dp instead of index because len = index + 1
    # Else we'll have to check whether index1 - 1 and index2 - 1 are out of bounds
    # This way we can do index1 + 1 and index2 + 1 instead which will always be valid
    dp = [[0] * (len(string2) + 1) for _ in range((len(string1) + 1))]

    for index1 in range(len(string1)):
      for index2 in range(len(string2)):
        if string1[index1] == string2[index2]:
          dp[index1 + 1][index2 + 1] = 1 + dp[index1][index2]
        else:
          len1 = dp[index1][index2 + 1]
          len2 = dp[index1 + 1][index2]
          dp[index1 + 1][index2 + 1] = max(len1, len2)

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, string1, string2):
    # Track length in the dp instead of index because len = index2 + 1
    # Else we'll have to check whether index2 - 1 is out of bounds
    # This way we can do index2 + 1 instead which will always be valid
    dp = [0] * (len(string2) + 1)

    for index1 in range(len(string1)):
      prev = dp[0]

      for index2 in range(len(string2)):
        curr = dp[index2 + 1]

        if string1[index1] == string2[index2]:
          dp[index2 + 1] = 1 + dp[index2]
        else:
          len1 = dp[index2 + 1]
          len2 = dp[index2]
          dp[index2 + 1] = max(len1, len2)

        prev = curr

    return dp[-1]

test_class(Solution4, examples)

from utils import test_class

# Find the longest common subsequence (LCS) for the two given strings
# LCS is the longest subsequence that is present in both the strings

examples = [
  {
    'input': ['abcd', 'bd'],
    'output': 2 # bd
  },
  {
    'input': ['aggtab', 'gxtxayb'],
    'output': 4 # gtab
  },
  {
    'input': ['', 'abcd'],
    'output': 0
  },
]

# Recursion
# Time Complexity: O(2^(n + m))
# Auxiliary Space: O(2^(n + m)) due to recursive stack
class Solution:
  def solve(self, string1, string2):
    return self.find_lcs(string1, string2, 0, 0)

  def find_lcs(self, string1, string2, index1, index2):
    if index1 == len(string1) or index2 == len(string2):
      return 0

    if string1[index1] == string2[index2]:
      return 1 + self.find_lcs(string1, string2, index1 + 1, index2 + 1)

    len1 = self.find_lcs(string1, string2, index1 + 1, index2)
    len2 = self.find_lcs(string1, string2, index1, index2 + 1)
    return max(len1, len2)

test_class(Solution, examples)

# Dynamic Programming with Memoization
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution2:
  def solve(self, string1, string2):
    self.lcs = [[-1] * len(string2) for _ in range(len(string1))]
    return self.find_lcs(string1, string2, 0, 0)

  def find_lcs(self, string1, string2, index1, index2):
    if index1 == len(string1) or index2 == len(string2):
      return 0

    if self.lcs[index1][index2] != -1:
      return self.lcs[index1][index2]

    if string1[index1] == string2[index2]:
      self.lcs[index1][index2] = \
        1 + self.find_lcs(string1, string2, index1 + 1, index2 + 1)
      return self.lcs[index1][index2]

    len1 = self.find_lcs(string1, string2, index1 + 1, index2)
    len2 = self.find_lcs(string1, string2, index1, index2 + 1)
    self.lcs[index1][index2] = max(len1, len2)
    return self.lcs[index1][index2]

test_class(Solution2, examples)

# Dynamic Programming with Tabulation
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution3:
  def solve(self, string1, string2):
    lcs = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          lcs[i + 1][j + 1] = 1 + lcs[i][j]
        else:
          lcs[i + 1][j + 1] = max(lcs[i + 1][j], lcs[i][j + 1])

    return lcs[len(string1)][len(string2)]

test_class(Solution3, examples)

# Tabulation with Space Optimization
# We need values of only two rows: lcs[i] and lcs[i + 1]
# That is current row and previous row
# Time Complexity: O(n * m)
# Auxiliary Space: O(m)
class Solution4:
  def solve(self, string1, string2):
    # Stores lcs[i] of previous solution
    prev = [0] * (len(string2) + 1)
    # Stores lcs[i + 1] of previous solution
    curr = [0] * (len(string2) + 1)

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          curr[j + 1] = 1 + prev[j]
        else:
          curr[j + 1] = max(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[len(string2)]

test_class(Solution4, examples)

from utils import test_class

# Find the length of the longest repeating subsequence for a given string
# Such that two subsequences don't have the same string char at the same position
examples = [
  {
    'input': ['abc'],
    'output': 0
  },
  {
    'input': ['aab'],
    'output': 1 # a (starting at index 0 & 1)
  },
  {
    'input': ['aabb'],
    'output': 2 # ab (starting at index 0 & 1)
  },
  {
    'input': ['axxxy'],
    'output': 2 # xx (starting at index 0 & 1)
  },
]

# Modification of longest common subsequence
# Find the lcs(str, str) where str is the given string
# with the restriction that when both the chars are same,
# they shouldn't be on the same index in the two strings
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    prev = [0] * (len(string) + 1)
    curr = [0] * (len(string) + 1)

    for i in range(len(string)):
      for j in range(len(string)):
        if string[i] == string[j] and i != j:
          curr[j + 1] = 1 + prev[j]
        else:
          curr[j + 1] = max(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[len(string)]

# Bottom-Up Memoization
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution2:
  def __init__(self):
    self.lrs = [[]]

  def find_lrs(self, string, index1, index2):
    if index1 < 0 or index2 < 0:
      return 0

    if self.lrs[index1][index2] != -1:
      return self.lrs[index1][index2]

    if string[index1] == string[index2] and index1 != index2:
      self.lrs[index1][index2] = 1 + self.find_lrs(string, index1 - 1, index2 - 1)
      return self.lrs[index1][index2]

    len1 = self.find_lrs(string, index1 - 1, index2)
    len2 = self.find_lrs(string, index1, index2 - 1)
    self.lrs[index1][index2] = max(len1, len2)
    return self.lrs[index1][index2]

  def solve(self, string):
    self.lrs = [[-1] * len(string) for _ in range(len(string))]
    return self.find_lrs(string, len(string) - 1, len(string) - 1)

# Top-down Memoization
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution3:
  def __init__(self):
    self.lrs = [[]]

  def find_lrs(self, string, index1, index2):
    if index1 == len(string) or index2 == len(string):
      return 0

    if self.lrs[index1][index2] != -1:
      return self.lrs[index1][index2]

    if string[index1] == string[index2] and index1 != index2:
      self.lrs[index1][index2] = 1 + self.find_lrs(string, index1 + 1, index2 + 1)
      return self.lrs[index1][index2]

    len1 = self.find_lrs(string, index1 + 1, index2)
    len2 = self.find_lrs(string, index1, index2 + 1)
    self.lrs[index1][index2] = max(len1, len2)
    return self.lrs[index1][index2]

  def solve(self, string):
    self.lrs = [[-1] * len(string) for _ in range(len(string))]
    return self.find_lrs(string, 0, 0)

test_class(Solution, examples)
test_class(Solution2, examples)
test_class(Solution3, examples)

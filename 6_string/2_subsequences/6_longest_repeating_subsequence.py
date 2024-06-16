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
# Auxiliary Space: O(n^2)
class Solution:
  def solve(self, string):
    lcs = [[0] * (len(string) + 1) for _ in range(len(string) + 1)]

    for i in range(len(string)):
      for j in range(len(string)):
        if string[i] == string[j] and i != j:
          lcs[i + 1][j + 1] = 1 + lcs[i][j]
        else:
          lcs[i + 1][j + 1] = max(lcs[i + 1][j], lcs[i][j + 1])

    return lcs[len(string)][len(string)]

test_class(Solution, examples)

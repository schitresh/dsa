from utils import test_class

examples = [
  {
    'input': ['abcd', 'bdef'],
    'output': 6 # Both strings can be subsequence of abcdef
  },
  {
    'input': ['aggtab', 'gxtxayb'],
    'output': 9 # Both strings can be subsequence of aggxtxayb or agxgtxayb
  },
  {
    'input': ['', 'abcd'],
    'output': 4 # Both strings can be subsequence of abcd
  },
]

# Time Complexity: O(2^(n * m))
# Space Complexity: O(n * m) due to recursive stack
class Solution:
  def find_lcs(self, string1, string2, index1, index2):
    if index1 == len(string1) or index2 == len(string2):
      return 0

    if string1[index1] == string2[index2]:
      return 1 + self.find_lcs(string1, string2, index1 + 1, index2 + 1)

    len1 = self.find_lcs(string1, string2, index1 + 1, index2)
    len2 = self.find_lcs(string1, string2, index1, index2 + 1)
    return max(len1, len2)

  def solve(self, string1, string2):
    return self.find_lcs(string1, string2, 0, 0)

from utils import test_class

# Find the length of the longest palindromic subsequence for a given string
# That is the longest subsequence that is also a palindrome
examples = [
  {
    'input': ['abc'],
    'output': 1 # a
  },
  {
    'input': ['bbabcbcab'],
    'output': 7 # babcbab
  },
  {
    'input': [''],
    'output': 0
  },
  {
    'input': ['abccba'],
    'output': 6 # abccba
  },
  {
    'input': ['daebfcghchbiaj'],
    'output': 7 # abcgcba
  }
]

# Recursive Solution
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def lps(self, string, left, right):
    if left == right:
      return 1

    # Middle chars are same, like cc in abccba
    if left + 1 == right and string[left] == string[right]:
      return 2

    if string[left] == string[right]:
      return 2 + self.lps(string, left + 1, right - 1)

    len1 = self.lps(string, left + 1, right)
    len2 = self.lps(string, left, right - 1)
    return max(len1, len2)

  def solve(self, string):
    if len(string) == 0: return 0
    return self.lps(string, 0, len(string) - 1)

# Similar to the longest common subsequence
# Find lcs of string and its reversed string
# Most optimized solution of lcs, other solutions are similar
# Time Complexity: O(n * m)
# Auxiliary Space: O(m)
class Solution2:
  def solve(self, string):
    rev_string = string[::-1]
    prev = [0] * (len(string) + 1)
    curr = [0] * (len(string) + 1)

    for i in range(len(string)):
      for j in range(len(string)):
        if string[i] == rev_string[j]:
          curr[j + 1] = 1 + prev[j]
        else:
          curr[j + 1] = max(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[-1]

test_class(Solution, examples)
test_class(Solution2, examples)

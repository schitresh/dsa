from utils import test_class

# Given two string s1 and s2 of same length, check whether s2 is a rotation of s1.

examples = [
  {
    'input': ['abcd', 'cdab'],
    'output': True,
  },
  {
    'input': ['abac', 'acabab'],
    'output': True,
  },
  {
    'input': ['aab', 'aba'],
    'output': True,
  },
  {
    'input': ['abcd', 'acbd'],
    'output': False,
  },
]

# Inbuilt Method
class Solution:
  def solve(self, string1, string2):
    string = string2 + string2
    return string1 in string

test_class(Solution, examples)

# Check for each position
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, string1, string2):
    for i in range(len(string2)):
      if string1[0] != string2[i]: continue

      idx1 = 0
      idx2 = i
      while idx1 < len(string1):
        if string1[idx1] != string2[idx2]: break

        idx1 += 1
        idx2 += 1
        if idx1 == len(string1): return True
        if idx2 == len(string2): idx2 = 0

    return False

test_class(Solution2, examples)

# KMP Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, string1, string2):
    lps = self.cal_lps(string1)

    idx1 = 0
    idx2 = 0

    while idx2 < len(string2):
      if string1[idx1] == string2[idx2]:
        idx1 += 1
        idx2 += 1
        if idx1 == len(string1): return True
        if idx2 == len(string2): idx2 = 0
      else:
        if idx1 == 0:
          idx2 += 1
        else:
          idx1 = lps[idx1 - 1]

    return False

  # Longest prefix which is also a suffix for every substring starting at index 0
  def cal_lps(self, pattern):
    lps = [0] * len(pattern)

    prefix = 0
    suffix = 1

    while suffix < len(pattern):
      # If the current char matches, then the matched length is prefix + 1 since the
      # prefix always starts from 0. That is lps[suffix] = matched_length
      if pattern[suffix] == pattern[prefix]:
        lps[suffix] = prefix + 1
        prefix += 1
        suffix += 1
      else:
        # If some part of the suffix matched, we need to check if the there exists any
        # suffix within the matched suffix that matches the prefix. If so, we have
        # already calculated that in the prefix. Since prefix - 1 = suffix - 1, we can
        # say that this sub-matched length is lps[prefix - 1] from where we should
        # continue matching.
        # For example, in abacxyababa, consider abac and abab. When we compare c & b, it
        # is not a match, but the lps is not 0 because the suffix ab within the original
        # suffix abab matches the prefix ab. Further which the new suffix aba matches
        # with the prefix.
        if prefix != 0:
          prefix = lps[prefix - 1]
        else:
          suffix += 1

    return lps

test_class(Solution3, examples)

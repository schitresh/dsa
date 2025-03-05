from utils import test_class

# Given a string, remove minimum number of chars so that
# the resultant string is a palindrome

examples = [
  {
    'input': ['aebcbda'],
    'output': 2 # abcba
  },
  {
    'input': ['abcdba'],
    'output': 1 # abcba
  },
  {
    'input': ['cabdebaf'],
    'output': 3 # abdba
  },
  {
    'input': ['aba'],
    'output': 0
  },
]

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), maximum depth of the recursion tree can be n
class Solution:
  def solve(self, string):
    return self.min_deletion(string, 0, len(string) - 1)

  def min_deletion(self, string, left, right):
    if left >= right:
      return 0

    if string[left] == string[right]:
      return self.min_deletion(string, left + 1, right - 1)

    count1 = self.min_deletion(string, left + 1, right)
    count2 = self.min_deletion(string, left, right - 1)
    return 1 + min(count1, count2)

test_class(Solution, examples)

# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution2:
  def solve(self, string):
    self.k = 0
    self.char_count = [[-1] * len(string) for _ in range(len(string))]
    return self.min_deletion(string, 0, len(string) - 1)

  def min_deletion(self, string, left, right):
    if left >= right:
      return 0

    if self.char_count[left][right] != -1:
      return self.char_count[left][right]

    if string[left] == string[right]:
      self.char_count[left][right] = self.min_deletion(string, left + 1, right - 1)
      return self.char_count[left][right]

    count1 = self.min_deletion(string, left + 1, right)
    count2 = self.min_deletion(string, left, right - 1)
    self.char_count[left][right] = 1 + min(count1, count2)
    return self.char_count[left][right]

test_class(Solution2, examples)

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), maximum depth of the recursion tree can be n
class Solution3:
  def solve(self, string):
    # Subtract longest palindromic subsequence
    return len(string) - self.lps_len(string)

  def lps_len(self, string):
    lps = [[0] * len(string) for _ in range(len(string))]

    for i in range(len(string)):
      lps[i][i] = 1

    for i in range(len(string) - 1):
      if string[i] == string[i + 1]:
        lps[i][i + 1] = 2
      else:
        lps[i][i + 1] = 1

    for substr_len in range(3, len(string) + 1):
      for l in range(len(string) - substr_len + 1):
        r = l + substr_len - 1

        if string[l] == string[r]:
          lps[l][r] = 2 + lps[l + 1][r - 1]
        else:
          lps[l][r] = max(lps[l + 1][r], lps[l][r - 1])

    return lps[0][len(string) - 1]

test_class(Solution3, examples)

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), maximum depth of the recursion tree can be n
class Solution4:
  def solve(self, string):
    # Subtract longest palindromic subsequence
    return len(string) - self.lps_len(string)

  def lps_len(self, string):
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

test_class(Solution4, examples)

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), maximum depth of the recursion tree can be n
class Solution5:
  def solve(self, string):
    curr = [0] * (len(string) + 1)
    prev = curr.copy()

    for i in range(len(string) - 2, -1, -1):
      for j in range(i + 1, len(string)):
        if string[i] == string[j]:
          curr[j + 1] = prev[j]
        else:
          curr[j + 1] = 1 + min(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[-1]

test_class(Solution5, examples)

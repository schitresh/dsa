from utils import test_class

# Find the length of the shortest string
# that has both the given strings as subsequences

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

# Closely related to longest common subsequence
# Find lcs of two given strings
# And insert non-lcs characters to the lcs in their original order in strings
# Consider 'aggtab' & 'gxtxayb', lcs of these is 'gtab'
# After inserting non-lcs chars of first string, we get 'aggtab'
# After inserting non-lcs chars of second string, we get 'aggxtxayb'
# So, resultant length = length of string1 + length of string2 - length of lcs
# Time Complexity: O(n * m)
# Auxiliary Space: O(m) to calculate lcs
class Solution:
  def solve(self, string1, string2):
    lcs_len = self.find_lcs_len(string1, string2)
    return len(string1) + len(string2) - lcs_len

  def find_lcs_len(self, string1, string2):
    prev = [0] * (len(string2) + 1)
    curr = [0] * (len(string2) + 1)

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          curr[j + 1] = 1 + prev[j]
        else:
          curr[j + 1] = max(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[len(string2)]

test_class(Solution, examples)

# Recursive Solution
# Time Complexity: O(2^(n + m))
# Auxiliary Space: O(n + m) for the recursive stack
class Solution2:
  def solve(self, string1, string2):
    return self.scs_len(string1, string2, len(string1) - 1, len(string2) - 1)

  def scs_len(self, string1, string2, index1, len2):
    # If string1 is fully iterated, remaining chars of string2 cannot be common
    # Hence return remaining length of string2, i.e. len2 + 1
    if index1 < 0:
      return len2 + 1

    # Same condition if string2 is fully iterated
    if len2 < 0:
      return index1 + 1

    if string1[index1] == string2[len2]:
      return 1 + self.scs_len(string1, string2, index1 - 1, len2 - 1)

    len1 = self.scs_len(string1, string2, index1 - 1, len2)
    len2 = self.scs_len(string1, string2, index1, len2 - 1)
    # Count the current char, and add the min scs length for rest of the strings
    return 1 + min(len1, len2)

test_class(Solution2, examples)

# Dynamic Programming for the recursive solution
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution3:
  def solve(self, string1, string2):
    scs = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    # If length of string2 is 0, then scs will be the length of string1
    for i in range(len(string1)):
      # Since i is the index, the length will be i + 1
      scs[i + 1][0] = i + 1

    # If length of string1 is 0, then scs will be the length of string2
    for j in range(len(string2)):
      scs[0][j + 1] = j + 1

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          scs[i + 1][j + 1] = 1 + scs[i][j]
        else:
          scs[i + 1][j + 1] = 1 + min(scs[i + 1][j], scs[i][j + 1])
        # print(scs[i], scs[i + 1])

    return scs[len(string1)][len(string2)]

test_class(Solution3, examples)

# Dynamic Programming with top down memoization
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m) for the recursive stack
class Solution4:
  def solve(self, string1, string2):
    self.scs = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    return self.scs_len(string1, string2, len(string1), len(string2))

  def scs_len(self, string1, string2, len1, len2):
    if len1 == 0 or len2 == 0:
      self.scs[len1][len2] = len1 + len2

    if self.scs[len1][len2] > 0:
      return self.scs[len1][len2]

    if string1[len1 - 1] == string2[len2 - 1]:
      self.scs[len1][len2] = 1 + self.scs_len(string1, string2, len1 - 1, len2 - 1)
      return self.scs[len1][len2]

    scs_len1 = self.scs_len(string1, string2, len1 - 1, len2)
    scs_len2 = self.scs_len(string1, string2, len1, len2 - 1)
    # Count the current char, and add the min scs length for rest of the strings
    self.scs[len1][len2] = 1 + min(scs_len1, scs_len2)
    return self.scs[len1][len2]

test_class(Solution4, examples)

# Dynamic Programming with space optimization
# Time Complexity: O(n * m)
# Auxiliary Space: O(m) for the recursive stack
class Solution5:
  def solve(self, string1, string2):
    # Stores scs[i] of previous solution
    prev = list(range(len(string2) + 1))
    # Stores scs[i + 1] of previous solution
    curr = prev.copy()

    for i in range(len(string1)):
      curr[0] = i + 1

      for j in range(len(string2)):
        if string1[i] == string2[j]:
          curr[j + 1] = 1 + prev[j]
        else:
          curr[j + 1] = 1 + min(curr[j], prev[j + 1])

      prev = curr.copy()

    return curr[len(string2)]

test_class(Solution5, examples)

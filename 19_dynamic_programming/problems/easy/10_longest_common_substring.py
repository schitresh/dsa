from utils import test_class

# Given two strings ‘s1‘ and ‘s2‘, find the length of the longest common substring

examples = [
  {
    'input': ['GeeksforGeeks', 'GeeksQuiz'],
    'output': 5,
    # Geeks
  },
  {
    'input': ['abcdxyz', 'xyzabcd'],
    'output': 4,
    # abcd
  },
  {
    'input': ['abc', ''],
    'output': 0
  },
]

# Naive Iteration
# Time Complexity: O(m * n * min(m, n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string1, string2):
    result = 0

    for i in range(len(string1)):
      for j in range(len(string2) - i):
        pos = 0
        curr = 0

        while i + pos < len(string1) and j + pos < len(string2):
          if string1[pos + i] == string2[pos + j]:
            curr += 1
            pos += 1
          else:
            break

        result = max(result, curr)

    return result

test_class(Solution, examples)

# Recursion
# Time Complexity: O(m * n * min(m, n))
# Auxiliary Space: O(min(m, n)), due to recursive stack
class Solution2:
  def solve(self, string1, string2):
    self.string1 = string1
    self.string2 = string2
    result = 0

    for i in range(len(string1)):
      for j in range(len(string2) - i):
        curr = self.common_substring(i, j)
        result = max(result, curr)

    return result

  def common_substring(self, index1, index2):
    if index1 == len(self.string1) or index2 == len(self.string2): return 0
    if self.string1[index1] != self.string2[index2]: return 0
    return 1 + self.common_substring(index1 + 1, index2 + 1)

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution3:
  def solve(self, string1, string2):
    # Longest Common Suffix
    lc_suffix = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    result = 0

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          lc_suffix[i + 1][j + 1] = 1 + lc_suffix[i][j]
          result = max(result, lc_suffix[i + 1][j + 1])
        else:
          lc_suffix[i + 1][j + 1] = 0

    return result

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, string1, string2):
    # Longest Common Suffix
    lc_suffix = [0] * (len(string2) + 1)
    result = 0

    for i in range(len(string1)):
      curr = [0] * (len(string2) + 1)

      for j in range(len(string2)):
        if string1[i] == string2[j]:
          curr[j + 1] = 1 + lc_suffix[j]
          result = max(result, curr[j + 1])
        else:
          curr[j + 1] = 0

      lc_suffix = curr

    return result

test_class(Solution4, examples)

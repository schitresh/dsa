from utils import test_class

# Count the number of possible decodings of the given digit sequence.
# Let 1 represent 'A', 2 represent 'B', and so on. Multiple interpretations can arise due
# to overlapping possibilities for how digits can be grouped into valid letter mappings.
# Consider the input string '123'. There are three valid ways to decode it:
# 'ABC': The grouping is (1, 2, 3) → 'A', ‘B', ‘C'
# 'AW': The grouping is (1, 23) → ‘A', ‘W'
# 'LC': The grouping is (12, 3) → ‘L', ‘C'
# Groupings containing invalid codes are not allowed (e.g., '0' by itself or numbers
# greater than '26'). For instance, the string '230' is invalid because '0' cannot stand
# alone, and '30' is greater than '26'.
# Find the total number of valid ways to decode a given string.

examples = [
  {
    'input': ['121'],
    'output': 3,
    # aba, au, la
  },
  {
    'input': ['1234'],
    'output': 3,
    # abcd, lcd, awd
  },
  {
    'input': ['230'],
    'output': 0,
    # All possibilities are invalid: (2, 3, 0), (2, 30), (23, 0)
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    return self.decode(0)

  def decode(self, pos):
    if pos >= len(self.string): return 1
    if self.string[pos] == '0': return 0

    way1 = self.decode(pos + 1)

    way2 = 0
    if pos + 1 < len(self.string):
      if int(self.string[pos: pos + 2]) <= 26:
        way2 = self.decode(pos + 2)

    return way1 + way2

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string):
    self.string = string
    self.memo = [None] * len(string)
    return self.decode(0)

  def decode(self, pos):
    if pos >= len(self.string): return 1
    if self.string[pos] == '0': return 0

    if self.memo[pos]:
      return self.memo[pos]

    way1 = self.decode(pos + 1)

    way2 = 0
    if pos + 1 < len(self.string):
      if int(self.string[pos: pos + 2]) <= 26:
        way2 = self.decode(pos + 2)

    self.memo[pos] = way1 + way2
    return self.memo[pos]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, string):
    dp = [0] * (len(string) + 1)
    # Base case: Empty string has one valid decoding
    dp[len(string)] = 1

    for pos in range(len(string) - 1, -1, -1):
      if string[pos] == '0': continue

      dp[pos] = dp[pos + 1]

      if pos + 1 < len(string):
        if int(string[pos: pos + 2]) <= 26:
          dp[pos] += dp[pos + 2]

    return dp[0]

test_class(Solution3, examples)

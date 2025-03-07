from utils import test_class

# Given a number n, count number of n length binary strings with consecutive 1’s in them.

examples = [
  {
    'input': [2],
    'output': 1,
    # Only 11 has consecutive 1s among 00, 01, 10, 11
  },
  {
    'input': [3],
    'output': 3,
    # 011, 110, 111
  },
  {
    'input': [5],
    'output': 19,
  },
]

# Generate all binary strings
# Time Complexity: O(2^n * n)
# 2^n to generate all binary strings and n to traverse each binary string to check
# consecutive 1s
# Auxiliary Space: O(n)
class Solution:
  def solve(self, num):
    return self.binary_strings('', num)

  def binary_strings(self, string, rem_len):
    if rem_len == 0:
      for i in range(len(string) - 1):
        if string[i : i + 2] == '11':
          return 1

      return 0

    count1 = self.binary_strings(string + '0', rem_len - 1)
    count2 = self.binary_strings(string + '1', rem_len - 1)
    return count1 + count2

test_class(Solution, examples)

# Todo: Dynamic Programming
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, num):
    return

test_class(Solution2, examples)

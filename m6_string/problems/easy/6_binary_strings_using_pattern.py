from utils import test_class

# Given a string containing of '0', '1', '?' (wildcard character), generate all binary
# strings that can be formed by replacing each wildcard character by '0' or '1'.

examples = [
  {
    'input': ['1??0?101'],
    'output': [
      '10000101',
      '10001101',
      '10100101',
      '10101101',
      '11000101',
      '11001101',
      '11100101',
      '11101101',
    ],
  },
]

# Todo
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    self.result = []

    return self.result

test_class(Solution, examples)

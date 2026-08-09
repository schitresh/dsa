from queue import Queue
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

# Recursion
# Time Complexity: O(2^n), since there are 2 possibilities at every stage
# Auxiliary Space: O(n^2), as a copy of string is created in every call
class Solution:
  def solve(self, string):
    self.string = string
    self.result = []

    self.binary_strings('', 0)

    return self.result

  def binary_strings(self, prefix, idx):
    if idx == len(self.string):
      self.result.append(prefix)
      return

    if self.string[idx] != '?':
      self.binary_strings(prefix + self.string[idx], idx + 1)
      return

    self.binary_strings(prefix + '0', idx + 1)
    self.binary_strings(prefix + '1', idx + 1)

test_class(Solution, examples)

# Using Queue
# Time Complexity: O(2^n), since there are 2 possibilities at every stage
# Auxiliary Space: O(n^2), as a copy of string is created in every call
class Solution2:
  def solve(self, string):
    result = []
    queue = Queue()
    queue.put('')

    while not queue.empty():
      prefix = queue.get()
      if len(prefix) == len(string):
        result.append(prefix)
        continue

      idx = len(prefix)
      if string[idx] != '?':
        queue.put(prefix + string[idx])
        continue

      queue.put(prefix + '0')
      queue.put(prefix + '1')

    return result

test_class(Solution2, examples)

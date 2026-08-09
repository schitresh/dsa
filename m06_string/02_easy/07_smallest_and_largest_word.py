from utils import test_class

# Given a string, find the minimum and the maximum length words in it.

examples = [
  {
    'input': ['This is a test string'],
    'output': ['a', 'string'],
  },
  {
    'input': ['abcdef a'],
    'output': ['a', 'abcdef'],
  },
  {
    'input': ['a abcdef'],
    'output': ['a', 'abcdef'],
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    min_start = 0
    min_len = len(string)
    max_start = 0
    max_len = 0

    start = 0
    for i in range(len(string) + 1):
      if i < len(string) and string[i] != ' ': continue

      if i - start < min_len:
        min_start = start
        min_len = i - start

      if i - start > max_len:
        max_start = start
        max_len = i - start

      start = i + 1

    smallest = string[min_start : min_start + min_len]
    largest = string[max_start : max_start + max_len]
    return [smallest, largest]

test_class(Solution, examples)

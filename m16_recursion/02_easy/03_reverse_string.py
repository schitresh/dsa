from utils import test_class

# Reverse a given string using recursion

examples = [
  {
    'input': ['abcd'],
    'output': 'dcba'
  },
]

# Brute Force
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    return self.reverse(len(string) - 1)

  def reverse(self, index):
    if index == -1: return ''

    return self.string[index] + self.reverse(index - 1)

test_class(Solution, examples)

# Process from both ends
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, string):
    self.string = list(string)
    self.reverse(0, len(string) - 1)
    return ''.join(self.string)

  def reverse(self, start, end):
    if start >= end: return

    self.string[start], self.string[end] = self.string[end], self.string[start]
    self.reverse(start + 1, end - 1)

test_class(Solution2, examples)

from utils import test_class

# Check if the given string is a palindrome.

examples = [
  {
    'input': ['abcdcba'],
    'output': True
  },
  {
    'input': ['abcddcba'],
    'output': True
  },
  {
    'input': ['abcdecba'],
    'output': False
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    return self.palindrome(0, len(string) - 1)

  def palindrome(self, start, end):
    if start >= end: return True
    if self.string[start] != self.string[end]: return False

    return self.palindrome(start + 1, end - 1)

test_class(Solution, examples)

from utils import test_class

# Given a string, check if it is a rotation of a palindrome
examples = [
  {
    'input': ['cdcbaab'],
    'output': True # rotation of abcdcba
  },
  {
    'input': ['cbaabcdd'],
    'output': True # rotation of dcbaabcd
  },
  {
    'input': ['baabcd'],
    'output': False
  },
    {
    'input': ['ababcdc'],
    'output': False
  },
]

# Time Complexity: O(n^2)
# Auxiliary Space: O(n) for storing rotated string
class Solution:
  def is_palindrome(self, string):
    left = 0
    right = len(string) - 1

    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

  def solve(self, string):
    for i in range(len(string)):
      rotated_string = string[i : ] + string[ : i]

      if self.is_palindrome(rotated_string):
        return True

    return False

# Todo: Using Mancher's algorithm
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def is_palindrome(self, string):
    return False

  def solve(self, string):
    return False

test_class(Solution, examples)
test_class(Solution2, examples)

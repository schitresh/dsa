from utils import test_class

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
    'input': ['abcdba'],
    'output': False
  },
    {
    'input': ['abcdcbd'],
    'output': False
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    left = 0
    right = len(string) - 1

    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

test_class(Solution, examples)

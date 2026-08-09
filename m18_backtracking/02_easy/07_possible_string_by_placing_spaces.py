from utils import test_class

# Given a string, print all the possible strings that can be made by placing spaces in
# between them.

examples = [
  {
    'input': ['abc'],
    'output': ['abc', 'ab c', 'a bc', 'a b c']
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    self.result = []
    self.traverse(string[0], 1)
    return self.result

  def traverse(self, string, index):
    if index == len(self.string):
      self.result.append(string)
      return

    self.traverse(string + self.string[index], index + 1)
    self.traverse(string + ' ' + self.string[index], index + 1)

test_class(Solution, examples)

from utils import test_class

# Given a string, generate all possible strings that can be made by placing spaces at
# different positions.

examples = [
  {
    'input': ['abc'],
    'output': ['a b c', 'a bc', 'ab c', 'abc'],
  },
]

# Generate all pairs
# Time Complexity: O(2^n)
# Auxiliary Space: O(n^2), due to recursive stack and since a new string is generated
# in each recursive call
class Solution:
  def solve(self, string):
    self.string = string
    self.result = []
    self.generate_strings(string[0], 1)
    return self.result

  def generate_strings(self, prefix, idx):
    if idx == len(self.string):
      self.result.append(prefix)
      return

    self.generate_strings(prefix + ' ' + self.string[idx], idx + 1)
    self.generate_strings(prefix + self.string[idx], idx + 1)

test_class(Solution, examples)

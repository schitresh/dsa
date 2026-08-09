from utils import test_class

# Given a string, generate all its subsequences. A string is said to be a subsequence
# of another string, if it can be obtained by deleting 0 or more character without
# changing its order.
# Total subsequences = 2^n - 1 (excluding empty string)

examples = [
  {
    'input': ['abcd'],
    'output': ['a', 'ab', 'abc', 'abcd', 'abd', 'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']
  }
]

# Generate for each length
# Time Complexity: O(2^n),
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.subsequences = []
    self.generate_subsequences(string, '', 0)
    return self.subsequences

  def generate_subsequences(self, string, prefix, index):
    for i in range(index, len(string)):
      subsequence = prefix + string[i]
      self.subsequences.append(subsequence)
      self.generate_subsequences(string, subsequence, i + 1)

test_class(Solution, examples)

# Including & Excluding
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, string):
    self.subsequences = []
    self.generate_subsequences(string, '', 0)
    return self.subsequences

  def generate_subsequences(self, string, prefix, index):
    if index == len(string):
      if len(prefix) > 0:
        self.subsequences.append(prefix)
      return

    # Include the current char
    self.generate_subsequences(string, prefix + string[index], index + 1)
    # Exclude the current char
    self.generate_subsequences(string, prefix, index + 1)

test_class(Solution2, examples)

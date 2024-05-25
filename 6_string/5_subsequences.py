from utils import test_class

# Generate all subsequences
# Total subsequences = 2n - 1
examples = [
  {
    'input': ['abcd'],
    'output': ['a', 'ab', 'abc', 'abcd', 'abd', 'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']
  }
]

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) due to recursive stack
class Solution:
  def __init__(self):
    self.subsequences = []

  def generate_subsequences(self, string, prefix, index):
    for i in range(index, len(string)):
      subsequence = prefix + string[i]
      self.subsequences.append(subsequence)
      self.generate_subsequences(string, subsequence, i + 1)

  def solve(self, string):
    self.generate_subsequences(string, '', 0)
    return self.subsequences

# Time Complexity: O(2^n)
# Space Complexity: O(n) due to recursive stack
class Solution2:
  def __init__(self):
    self.subsequences = []

  def generate_subsequences(self, string, prefix, index):
    if index == len(string):
      if len(prefix) > 0:
        self.subsequences.append(prefix)
      return

    # Include the current char
    self.generate_subsequences(string, prefix + string[index], index + 1)
    # Exclude the current char
    self.generate_subsequences(string, prefix, index + 1)

  def solve(self, string):
    self.generate_subsequences(string, '', 0)
    return self.subsequences

test_class(Solution, examples)
test_class(Solution2, examples)

from utils import test_class

# Given a string S, print all permutations of a given string.
# A permutation (also called 'arrangement number' or 'order') is a rearrangement
# of the elements of an ordered list S into a one-to-one correspondence with S itself.
# A string of length N has N! permutations.

examples = [
  {
    'input': ['abc'],
    'output': ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
  },
  {
    'input': ['xy'],
    'output': ['xy', 'yx']
  },
]

# Backtracking
# It give duplicate permutations if there are repeating characters in the string
# Time Complexity: O(n * n!)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    self.permutations = []
    self.permute(string, 0)
    return self.permutations

  def permute(self, string, index):
    if index == len(string) - 1:
      self.permutations.append(string)
      return

    for j in range(index, len(string)):
      string = self.swap(string, index, j)
      self.permute(string, index + 1)
      # Backtrack
      string = self.swap(string, index, j)

  def swap(self, string, i, j):
    string = list(string)
    string[i], string[j] = string[j], string[i]
    return ''.join(string)

test_class(Solution, examples)

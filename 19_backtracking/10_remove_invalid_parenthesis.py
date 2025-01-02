from queue import Queue
from utils import test_class

# An expression will be given which can contain open and close parentheses
# and optionally some characters, no other operator will be there in string.
# We need to remove minimum number of parentheses to make the input string valid.
# If more than one valid output are possible removing same number of parentheses,
# then print all such output.

examples = [
  {
    'input': ['()())()'],
    'output': ['()()()', '(())()']
  },
  {
    'input': ['(v)())()'],
    'output': ['(v)()()', '(v())()']
  },
  {
    'input': ['(((((()))'],
    'output': ['((()))']
  },
]

# Using DFS
# Time Complexity: O(b^d) = O(2^n)
# where b is the branching factor (average number of child nodes per node)
# and d is the depth of the search tree
# Here, the branching factor is at most 2 (either remove or keep parenthesis at each pos)
# Auxiliary Space: O(2^n), as there can be upto 2^n valid combination
class Solution:
  def solve(self, string):
    self.string = list(string)
    self.valid_strings = []
    self.max_valid_len = 0

    self.check_parenthesis('', 0)

    return self.valid_strings

  def check_parenthesis(self, substring, pos):
    if pos == len(self.string):
      if not self.is_valid(substring): return

      if len(substring) > self.max_valid_len:
        self.max_valid_len = len(substring)
        self.valid_strings = [substring]
      elif len(substring) == self.max_valid_len:
        if substring not in self.valid_strings:
          self.valid_strings.append(substring)
      return

    self.check_parenthesis(substring + self.string[pos], pos + 1)
    self.check_parenthesis(substring, pos + 1)

  def is_valid(self, string):
    count = 0
    string = list(string)

    for char in string:
      if char == '(': count += 1
      elif char == ')': count -= 1

      if count < 0: return False

    return count == 0

test_class(Solution, examples)

# Using BFS
# Time Complexity: O(b^d) = O(2^n)
# where b is the branching factor (average number of child nodes per node)
# and d is the depth of the search tree
# Here, the branching factor is at most 2 (either remove or keep parenthesis at each pos)
# Auxiliary Space: O(2^n), as there can be upto 2^n valid combination
class Solution2:
  def solve(self, string):
    valid_strings = []

    queue = Queue()
    visited = set()

    queue.put(string)
    visited.add(string)
    level = False

    while not queue.empty():
      substring = queue.get()

      if self.is_valid(substring):
        valid_strings.append(substring)
        level = True

      # If the level has reached where a valid string is found
      # then don't break the string furthur down because we want minimum removals
      if level: continue

      for i in range(len(substring) - 1, -1, -1):
        if substring[i] == '(' or substring[i] == ')':
          temp = substring[0 : i] + substring[i + 1 : ]
          if temp not in visited:
            queue.put(temp)
            visited.add(temp)

    return valid_strings

  def is_valid(self, string):
    count = 0
    string = list(string)

    for char in string:
      if char == '(': count += 1
      elif char == ')': count -= 1

      if count < 0: return False

    return count == 0

test_class(Solution2, examples)

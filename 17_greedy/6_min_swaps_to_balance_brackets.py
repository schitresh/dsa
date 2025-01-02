from utils import test_class

# Given a string of 2N characters consisting of N [ brackets & N ] brackets.
# A string is considered balanced if it can be represented in the form S2[S1]
# where S1 and S2 are balanced strings.
# An unbalanced string can be balanced by swapping adjacent characters.
# Calculate the minimum number of adjacent swaps necessary to make a string balanced.

examples = [
  {
    'input': ['[]][]['],
    'output': 2
  },
  {
    'input': ['][]]][[['],
    'output': 7
  },
  {
    'input': ['[[][]]'],
    'output': 0
  },
]

# Naive approach: Swap each bracket individually
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    string = list(string)
    swaps = 0
    count = 0

    for i in range(len(string)):
      if string[i] == '[':
        count += 1
      else:
        count -= 1

      if count < 0:
        j = string.index('[', i + 1)
        self.swap_brackets(string, i, j)
        # Since only adjancent swaps are allowed
        swaps += j - i
        # Reset count to current bracket, i.e. '['
        count = 1

    return swaps

  # Swap adjacent chars
  # Start swapping from j where '[' is found to bring it at i
  def swap_brackets(self, string, i, j):
    temp = string[j]
    for k in range(j, i, -1):
      string[k] = string[k - 1]
    string[i] = temp

test_class(Solution, examples)

# Optmizied approach: Track the positions of '['
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string):
    string = list(string)
    swaps = 0
    count = 0

    # Keep track of '['
    position = []
    for i in range(len(string)):
      if string[i] == '[':
        position.append(i)

    # To track position of next '['
    position_index = 0

    for i in range(len(string)):
      if string[i] == '[':
        count += 1
        position_index += 1
      else:
        count -= 1

      if count < 0:
        bracket_index = position[position_index]
        # Swap till next position of '[' with the current ']' at i
        swaps += bracket_index - i
        string[i], string[bracket_index] = string[bracket_index], string[i]
        position_index += 1
        count = 1

    return swaps

test_class(Solution2, examples)

# Optmizied approach: Without trackings the positions of '['
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, string):
    string = list(string)
    swaps = 0
    imbalance = 0

    for char in string:
      if char == '[':
        imbalance -= 1
      else:
        imbalance += 1
        # Essentially, imbalance indicates the extra number of '['
        # And we need to swap them till the brackets are balanced, i.e. imbalance is 0
        if imbalance > 0:
          swaps += imbalance

    return swaps

test_class(Solution3, examples)

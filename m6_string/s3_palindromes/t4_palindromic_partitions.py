from utils import test_class

# Find all the possible palindromic partitions of the given string
# Generate all the partitions such that
# The string is divided into substrings that are all palindromes
examples = [
  {
    'input': ['abcba'],
    'output': [['a', 'b', 'c', 'b', 'a'], ['a', 'bcb', 'a'], ['abcba']]
  },
  {
    'input': ['abba'],
    'output': [['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']]
  },
  {
    'input': ['abcd'],
    'output': [['a', 'b', 'c', 'd']]
  },
  {
    'input': ['abaxyyx'],
    'output': [
      ['a', 'b', 'a', 'x', 'y', 'y', 'x'],
      ['a', 'b', 'a', 'x', 'yy', 'x'],
      ['a', 'b', 'a', 'xyyx'],
      ['aba', 'x', 'y', 'y', 'x'],
      ['aba', 'x', 'yy', 'x'],
      ['aba', 'xyyx'],
    ]
  },
]

# Using Bit Manipulation
# If there are n chars, there are n - 1 positions to cut the string
# Each of these positions can be given a binary number
# 1 if a cut is made in that position else 0
# This gives 2^(n - 1) partitions
# Time Complexity: O(n * 2^n)
# Auxiliary Space: O(2^n) to store all the partitions
class Solution:
  def __init__(self):
    self.partitions = []

  def is_palidromic(self, partition):
    for substr in partition:
      left = 0
      right = len(substr) - 1

      while left < right:
        if substr[left] != substr[right]:
          return False

        left += 1
        right -= 1

    return True

  def generate_partition(self, string, bit_string):
    partition = []
    sub_string = string[0]

    for i in range(len(bit_string)):
      # If the bit is 0, don't cut at this position
      # and include the next character directly
      if bit_string[i] == '0':
        sub_string += string[i + 1]
      # If the bit is 1, put a cut, i.e. add the current substring to partitions
      # and start a new substring
      else:
        partition.append(sub_string)
        sub_string = string[i + 1]

    partition.append(sub_string)
    if self.is_palidromic(partition):
      self.partitions.append(partition)

  def bit_manipulation(self, string, bit_string):
    if len(bit_string) == len(string) - 1:
      self.generate_partition(string, bit_string)
      return

    self.bit_manipulation(string, bit_string + '1')
    self.bit_manipulation(string, bit_string + '0')

  def solve(self, string):
    bit_string = ''
    self.bit_manipulation(string, bit_string)
    return self.partitions


# Recursion and Backtracking
# Time Complexity: O(n * 2^n)
# Auxiliary Space: O(2^n) to store all the partitions
class Solution2:
  def __init__(self):
    self.partitions = []

  def is_palidrome(self, string):
    left = 0
    right = len(string) - 1

    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

  def partition(self, string, index, curr):
    if index == len(string):
      # Create a new array using list to avoid reference to the original array
      self.partitions.append(list(curr))
      return

    sub_string = ''

    for i in range(index, len(string)):
      sub_string += string[i]

      if self.is_palidrome(sub_string):
        self.partition(string, i + 1, curr + [sub_string])

  def solve(self, string):
    self.partition(string, 0, [])
    return self.partitions

test_class(Solution, examples)
test_class(Solution2, examples)

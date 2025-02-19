from queue import LifoQueue
from utils import test_class

# Given a string, reverse the individual words using stack.

examples = [
  {
    'input': ['Hello World'],
    'output': 'olleH dlroW',
  },
  {
    'input': ['Reverse'],
    'output': 'esreveR',
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    string = list(string)
    stack = LifoQueue()
    start = 0

    for i in range(len(string)):
      is_last_char = i == len(string) - 1

      if string[i] == ' ' or is_last_char:
        if is_last_char: stack.put(string[i])

        while not stack.empty():
          string[start] = stack.get()
          start += 1

        start += 1
      else:
        stack.put(string[i])

    return ''.join(string)


test_class(Solution, examples)

from queue import LifoQueue
from utils import test_class

# Given a string representing an expression containing various types of brackets:
# {}, (), and [], determine whether the brackets are balanced or not. A balanced
# expression is one where every opening bracket has a corresponding closing bracket in
# the correct order.

examples = [
  {
    'input': ['[{()}]'],
    'output': True,
  },
  {
    'input': ['[()()]{}'],
    'output': True,
  },
  {
    'input': ['([]'],
    'output': False,
  },
  {
    'input': ['([{]})'],
    'output': False,
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, exp):
    stack = LifoQueue()

    for char in exp:
      if char in ('(', '{', '['):
        stack.put(char)
      elif stack.empty():
        return False
      else:
        top = stack.get()
        if top != self.opening_bracket(char):
          return False

    return stack.empty()

  def opening_bracket(self, char):
    if char == ')': return '('
    if char == '}': return '{'
    if char == ']': return '['
    return None

test_class(Solution, examples)

# Keep track of top
# Instead of using actual stack, use the input string itself to simulate stack behavior.
# Use a top variable to keep track of the top of this virtual stack.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, exp):
    exp = list(exp)
    top = -1

    for char in exp:
      if top < 0 or exp[top] != self.opening_bracket(char):
        top += 1
        exp[top] = char
      else:
        top -= 1

    return top == -1

  def opening_bracket(self, char):
    if char == ')': return '('
    if char == '}': return '{'
    if char == ']': return '['
    return None

test_class(Solution2, examples)

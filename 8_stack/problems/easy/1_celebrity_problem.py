from queue import LifoQueue
from utils import test_class

# Given a square matrix of size n x n such that mat[i][j] = 1 means ith person knows jth
# person, find the celebrity. A celebrity is a person who is known to all but does not
# know anyone. Return the index of the celebrity, if there is no celebrity return -1.
# M[i][i] will always be 0.

examples = [
  {
    'input': [[[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]],
    'output': 2,
  },
  {
    'input': [[[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]],
    'output': -1,
  },
  {
    'input': [[[0, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0]]],
    'output': 2,
  },
]

# Hashing
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, matrix):
    in_degree = [0] * len(matrix)
    out_degree = [0] * len(matrix)

    for i in range(len(matrix)):
      for j in range(len(matrix)):
        if matrix[i][j]: out_degree[i] += 1
        if matrix[j][i]: in_degree[i] += 1

    for i in range(len(matrix)):
      # If the person doesn't know anyone and everyone (expect himself) knows him
      if out_degree[i] == 0 and in_degree[i] == len(matrix) - 1:
        return i

    return -1

test_class(Solution, examples)

# Stack
# If A knows B, then A can’t be a celebrity. Discard A, and B may be celebrity.
# If A doesn’t know B, then B can’t be a celebrity. Discard B, and A may be celebrity.
# Repeat these steps till there is only one person. Ensure the remained person is a
# celebrity.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, matrix):
    celebrity = -1
    stack = LifoQueue()

    for i in range(len(matrix)):
      stack.put(i)

    while len(stack.queue) > 1:
      person1 = stack.get()
      person2 = stack.get()

      if matrix[person1][person2]:
        stack.put(person2)
      else:
        stack.put(person1)

    candidate = stack.get()
    for i in range(len(matrix)):
      if i == candidate: continue
      # If candidate knows any person or the person doesn't know the candidate, then there
      # is no celebrity
      if matrix[candidate][i] or not matrix[i][candidate]:
        return -1

    return candidate

test_class(Solution2, examples)

# Two Pointers
# Use two pointers, one from the start (A) and one from the end (B). If A knows B, then
# A must not be the celebrity. Else, B must not be the celebrity. At the end of the loop,
# only one index will be left as a celebrity. Go through each person again and check
# whether this is the celebrity.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, matrix):
    left = 0
    right = len(matrix) - 1

    while left < right:
      if matrix[left][right] == 1:
        left += 1
      else:
        right -= 1

    candidate = left
    for i in range(len(matrix)):
      if i == candidate: continue
      # If candidate knows any person or the person doesn't know the candidate, then there
      # is no celebrity
      if matrix[candidate][i] or not matrix[i][candidate]:
        return -1

    return candidate

test_class(Solution3, examples)

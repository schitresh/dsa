from utils import test_class

# Given a binary tree, check if it has heap property or not.
# Binary tree needs to fulfil the following two conditions for being a heap:
# 1. It should be a complete tree, i.e. all levels except the last should be full.
# 2. Every node’s value should be greater than or equal to its child node (considering
# max-heap).

examples = [
  {
    'input': [[5, 4, 3, 2, 1]],
    'output': [1, 2, 3, 4, 5],
  },
  {
    'input': [[5, 6, 3, 2, 1, 4]],
    'output': [1, 2, 3, 4, 5, 6],
  },
  {
    'input': [[9, 4, 3, 8, 10, 2, 5]],
    'output': [2, 3, 4, 5, 8, 9, 10],
  }
]

# Todo
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution:
  def solve(self, tree):
    return

test_class(Solution, examples)

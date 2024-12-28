from utils import test_class

# Given an n x n matrix, where every row and column is sorted in increasing order.
# Given a key, search whether this key is in the matrix.

examples = [
  {
    'input': [50, [
      [10, 20, 30, 40],
      [15, 25, 35, 45],
      [27, 29, 37, 48],
      [32, 33, 39, 50]
    ]],
    'output': [3, 3],
  },
  {
    'input': [29, [
      [10, 20, 30, 40],
      [15, 25, 35, 45],
      [27, 29, 37, 48],
      [32, 33, 39, 50]
    ]],
    'output': [2, 1],
  },
]

# Time Complexity: O(n * n(log(n)))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, key, matrix):
    for row in range(len(matrix)):
      if key < matrix[row][0] or matrix[row][-1] < key: continue
      left = 0
      right = len(matrix[0]) - 1

      while left <= right:
        col = left + (right - left) // 2
        item = matrix[row][col]

        if item < key: left = col + 1
        elif item > key: right = col - 1
        else: return [row, col]

test_class(Solution, examples)

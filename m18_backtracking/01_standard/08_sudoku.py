from utils import test_class

# Given a partially filled 9×9 2D array, assign digits (from 1 to 9) to the empty cells
# so that every row, column, and subgrid of size 3×3 contains exactly one instance
# of the digits from 1 to 9.

examples = [
  {
    'input': [[
      [3, 0, 6, 5, 0, 8, 4, 0, 0],
      [5, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 7, 0, 0, 0, 0, 3, 1],
      [0, 0, 3, 0, 1, 0, 0, 8, 0],
      [9, 0, 0, 8, 6, 3, 0, 0, 5],
      [0, 5, 0, 0, 9, 0, 6, 0, 0],
      [1, 3, 0, 0, 0, 0, 2, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]],
    'output': [
      [3, 1, 6, 5, 7, 8, 4, 9, 2],
      [5, 2, 9, 1, 3, 4, 7, 6, 8],
      [4, 8, 7, 6, 2, 9, 5, 3, 1],
      [2, 6, 3, 4, 1, 5, 9, 8, 7],
      [9, 7, 4, 8, 6, 3, 1, 2, 5],
      [8, 5, 1, 7, 9, 2, 6, 4, 3],
      [1, 3, 8, 9, 4, 7, 2, 5, 6],
      [6, 9, 2, 3, 5, 1, 8, 7, 4],
      [7, 4, 5, 2, 8, 6, 3, 1, 9],
    ]
  },
  {
    'input': [[
      [3, 1, 6, 5, 7, 8, 4, 9, 2],
      [5, 2, 9, 1, 3, 4, 7, 6, 8],
      [4, 8, 7, 6, 2, 9, 5, 3, 1],
      [2, 6, 3, 0, 1, 5, 9, 8, 7],
      [9, 7, 4, 8, 6, 0, 1, 2, 5],
      [8, 5, 1, 7, 9, 2, 6, 4, 3],
      [1, 3, 8, 0, 4, 7, 2, 0, 6],
      [6, 9, 2, 3, 5, 1, 8, 7, 4],
      [7, 4, 5, 0, 8, 6, 3, 1, 0],
    ]],
    'output': [
      [3, 1, 6, 5, 7, 8, 4, 9, 2],
      [5, 2, 9, 1, 3, 4, 7, 6, 8],
      [4, 8, 7, 6, 2, 9, 5, 3, 1],
      [2, 6, 3, 4, 1, 5, 9, 8, 7],
      [9, 7, 4, 8, 6, 3, 1, 2, 5],
      [8, 5, 1, 7, 9, 2, 6, 4, 3],
      [1, 3, 8, 9, 4, 7, 2, 5, 6],
      [6, 9, 2, 3, 5, 1, 8, 7, 4],
      [7, 4, 5, 2, 8, 6, 3, 1, 9],
    ]
  },
]

# Using Backtracking
# Time Complexity: O(9^(n^2)), for every unassigned index, there are 9 possible options
# Auxiliary Space: O(1)
class Solution:
  def solve(self, matrix):
    self.matrix = matrix
    self.sudoku(0, 0)
    return self.matrix

  def sudoku(self, row, col):
    # If the current row is iterated, go to the next row
    if col == 9:
      row += 1
      col = 0

    if row == 9:
      return True

    if self.matrix[row][col] > 0:
      return self.sudoku(row, col + 1)

    for num in range(1, 10):
      if not self.is_safe(row, col, num): continue

      self.matrix[row][col] = num
      if self.sudoku(row, col): return True
      self.matrix[row][col] = 0

    return False

  def is_safe(self, row, col, num):
    for i in range(9):
      if self.matrix[row][i] == num: return False
      if self.matrix[i][col] == num: return False

    start_row = (row // 3) * 3 # or (row - row % 3)
    start_col = (col // 3) * 3 # or (col - col % 3)
    for i in range(3):
      for j in range(3):
        if self.matrix[start_row + i][start_col + j] == num:
          return False

    return True

test_class(Solution, examples)

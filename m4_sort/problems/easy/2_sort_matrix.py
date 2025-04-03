from utils import test_class

# Given a m x n matrix, sort the matrix in strict order. Here, strict order means that
# the matrix is sorted in a way such that all elements in a row are sorted in increasing
# order. For row i, the first element is greater than or equal to the last element of
# row i-1.

examples = [
  {
    'input': [[
      [5, 4, 7],
      [1, 3, 8],
    ]],
    'output': [
      [1, 3, 4],
      [5, 7, 8],
    ],
  },
  {
    'input': [[
      [5, 4, 7],
      [1, 3, 8],
      [2, 9, 6],
    ]],
    'output': [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
  },
]

# Selection Sort
# Time Complexity: O((m * n)^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])
    size = row_size * col_size

    for i in range(size):
      row_i = i // col_size
      col_i = i % col_size
      min_row = row_i
      min_col = col_i

      for j in range(i + 1, size):
        row_j = j // col_size
        col_j = j % col_size

        if matrix[row_j][col_j] < matrix[min_row][min_col]:
          min_row = row_j
          min_col = col_j

      matrix[row_i][col_i], matrix[min_row][min_col] = \
        matrix[min_row][min_col], matrix[row_i][col_i]

    return matrix

test_class(Solution, examples)

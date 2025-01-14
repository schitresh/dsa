from utils import test_class

# Given a n by n board where n is of form 2k where k >= 1 (Basically n is a power of 2
# with minimum value as 2). The board has one missing cell (of size 1 x 1). Fill the
# board using L shaped tiles. A L shaped tile is a 2 x 2 square with one cell of size
# 1 × 1 missing.

examples = [
  {
    'input': [2, [0, 0]], # n, missing cell
    'output': [[-1, 1], [1, 1]], # tile numbers, -1 for missing cell
  },
  {
    'input': [4, [0, 0]],
    'output': [
      [-1, 3, 2, 2],
      [3, 3, 1, 2],
      [4, 1, 1, 5],
      [4, 4, 5, 5],
    ],
  }
]

# Todo
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, num, missing_cell):
    self.num = num
    self.board = [[0] * num for _ in range(num)]
    self.board[missing_cell[0]][missing_cell[1]] = -1

    self.fill_board(0, 0)
    return self.board

  def fill_board(self, left, right):
    return

test_class(Solution, examples)

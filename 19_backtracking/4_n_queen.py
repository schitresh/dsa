from utils import test_class

# The N Queen is the problem of placing N chess queens on an N×N chessboard
# so that no two queens attack each other.

examples = [
  {
    'input': [4],
    'output': [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
  },
]

# Backtracking
# Time Complexity: O(n!)
# Auxiliary Space: O(n^2), if board is included
class Solution:
  def solve(self, size):
    self.size = size
    self.moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]
    self.board = [[0] * size for _ in range(size)]

    self.place_in_row(0)

    return self.board

  def place_in_row(self, row):
    # We need N queens in N * N board and each queen need to be placed in separate rows
    # That means each row will have one queen
    # Hence, if we've completed N rows, N queens are placed
    if row == self.size: return True

    for col in range(self.size):
      if not self.is_safe(row, col): continue

      self.board[row][col] = 1
      if self.place_in_row(row + 1): return True
      self.board[row][col] = 0

    return False

  def is_safe(self, row, col):
    for move in self.moves:
      new_row = row + move[0]
      new_col = col + move[1]

      while self.valid_move(new_row, new_col):
        if self.board[new_row][new_col] == 1:
          return False

        new_row = new_row + move[0]
        new_col = new_col + move[1]

    return True

  def valid_move(self, row, col):
    within_limits = 0 <= row < self.size and 0 <= col < self.size
    return within_limits

test_class(Solution, examples)

# Backtracking with optimization to check safety of the queen
# Time Complexity: O(n!)
# Auxiliary Space: O(n^2), if board is included
class Solution2:
  def solve(self, size):
    self.size = size
    self.moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]
    self.board = [[0] * size for _ in range(size)]

    self.place_in_row(0)

    return self.board

  def place_in_row(self, row):
    # We need N queens in N * N board and each queen need to be placed in separate rows
    # That means each row will have one queen
    # Hence, if we've completed N rows, N queens are placed
    if row == self.size: return True

    for col in range(self.size):
      if not self.is_safe(row, col): continue

      self.board[row][col] = 1
      if self.place_in_row(row + 1): return True
      self.board[row][col] = 0

    return False

  # Since we're placing queens row by row, no need to check later rows
  # We need to check only for rows & diagonals before the current position
  # And need to check rows for current column only, since that's where queen can attack
  def is_safe(self, row, col):
    # Check all the upper rows for current column
    for i in range(row):
      if self.board[i][col] == 1: return False

    # Check left diagonal on the upper side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
      if self.board[i][j] == 1: return False

    # Check right diagonal on the upper side
    for i, j in zip(range(row, -1, -1), range(col, self.size)):
      if self.board[i][j] == 1: return False

    return True

  def valid_move(self, row, col):
    within_limits = 0 <= row < self.size and 0 <= col < self.size
    return within_limits

test_class(Solution2, examples)

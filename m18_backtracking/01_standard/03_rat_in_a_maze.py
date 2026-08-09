from utils import test_class

# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach
# the destination at (N – 1, N – 1). Find all the possible paths that the rat can take
# to reach from source to destination. Return the list of paths in lexicographically
# increasing order.
# The directions in which the rat can move are U(up), D(down), L(left), R(right).
# Value 0 at a cell in the matrix represents that it is blocked and value 1 represents
# that rat can be travel through it. In a path, no cell can be visited more than one
# time. If the source cell is 0, the rat cannot move to any other cell.

examples = [
  {
    'input': [[
      [1, 0, 0, 0],
      [1, 1, 0, 1],
      [1, 1, 0, 0],
      [0, 1, 1, 1]
    ]],
    'output': ['ddrdrr', 'drddrr']
  },
]

# Backtracking
# Time Complexity: O(3^(m * n))
# Because we have to try 3 different directions for each cell
# We won't check the cell from which we have visited in the last move
# Auxiliary Space: O(m * n), maximum depth of the recursion tree
class Solution:
  def solve(self, maze):
    self.moves = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    self.maze = maze
    self.rows = len(maze)
    self.cols = len(maze[0])
    self.paths = []

    self.travel('', 0, 0)

    return self.paths

  def travel(self, path, row, col):
    if row == self.rows - 1 and col == self.cols -1:
      self.paths.append(path)
      return

    # Mark the current cell as blocked to avoid looping endlessly
    self.maze[row][col] = 0

    for move in self.moves:
      new_row = row + move[0]
      new_col = col + move[1]

      if not self.valid_move(new_row, new_col): continue

      new_path = path + self.move_name(move)
      self.travel(new_path, new_row, new_col)

    # Mark the current cell as unblocked
    self.maze[row][col] = 1

  def valid_move(self, row, col):
    within_limits = 0 <= row < self.rows and 0 <= col < self.cols
    return within_limits and self.maze[row][col] == 1

  def move_name(self, move):
    # This is according to matrix(row, col), and not graph(x,y)
    if move == [1, 0]: return 'd'
    if move == [0, -1]: return 'r'
    if move == [-1, 0]: return 'u'
    if move == [0, 1]: return 'r'

test_class(Solution, examples)

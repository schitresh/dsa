import random
from utils import test_class

# Knight's Tour
# Given a N * N board with the Knight placed on the first block of an empty board.
# Knight must visit each square exactly once, moving according to the rules of chess.
# Print the order of each cell in which they are visited.

examples = [
  {
    'input': [8],
    'output': [
      [ 0, 59, 38, 33, 30, 17,  8, 63],
      [37, 34, 31, 60,  9, 62, 29, 16],
      [58,  1, 36, 39, 32, 27, 18,  7],
      [35, 48, 41, 26, 61, 10, 15, 28],
      [42, 57,  2, 49, 40, 23,  6, 19],
      [47, 50, 45, 54, 25, 20, 11, 14],
      [56, 43, 52,  3, 22, 13, 24,  5],
      [51, 46, 55, 44, 53,  4, 21, 12],
    ]
  },
]

# Backtracking
# It may take some time to run due to its large time complexity
# Time Complexity: O(8^(n^2)), there are n^2 cells and 8 possible moves to choose from
# Auxiliary Space: O(n^2)
class Solution:
  def solve(self, size):
    self.size = size
    self.board = [[-1] * size for _ in range(size)]
    self.moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

    # Since the knight is initially at the first block
    self.board[0][0] = 0
    # Counter for knight's position
    pos = 1
    self.travel(0, 0, pos)

    return self.board

  def travel(self, x, y, pos):
    if pos == self.size**2: return True

    for move in self.moves:
      new_x = x + move[0]
      new_y = y + move[1]

      if self.valid_move(new_x, new_y):
        self.board[new_x][new_y] = pos
        if self.travel(new_x, new_y, pos + 1): return True
        self.board[new_x][new_y] = -1

    return False

  def valid_move(self, x, y):
    within_limits = (x >= 0 and x < self.size) and (y >= 0 and y < self.size)
    if within_limits and self.board[x][y] == -1: return True
    return False

test_class(Solution, examples)

# Warnsdorff's Algorithm
# 1. We can start from any initial position of the knight on the board
# 2. We always move to an adjacent, unvisited square with minimal degree
# i.e. minimum number of unvisited adjacent squares
# Time Complexity: O(8^(n^2))
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, size):
    self.size = size
    self.moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

    board = False
    while not board:
      board = self.tour()

    return board

  def tour(self):
    self.board = [[-1] * self.size for _ in range(self.size)]
    source_x = 0
    source_y = 0
    # Since the knight is initially at the first block
    self.board[source_x][source_y] = 0

    x = source_x
    y = source_y
    for _ in range(self.size * self.size - 1):
      cell = self.next_move(x, y)
      if cell: x, y = cell
      else: return False

    if not self.is_neighbor(x, y, source_x, source_y): return False
    return self.board

  def valid_move(self, x, y):
    within_limits = (x >= 0 and x < self.size) and (y >= 0 and y < self.size)
    if within_limits and self.board[x][y] == -1: return True
    return False

  def degree(self, x, y):
    count = 0

    for move in self.moves:
      new_x = x + move[0]
      new_y = y + move[1]
      if self.valid_move(new_x, new_y): count += 1

    return count

  def next_move(self, x, y):
    min_degree_index = -1
    min_degree = 9
    start = random.randint(0, 1000) % self.size

    for count in range(self.size):
      move_index = (start + count) % 8
      move = self.moves[move_index]
      new_x = x + move[0]
      new_y = y + move[1]
      new_degree = self.degree(new_x, new_y)

      if self.valid_move(new_x, new_y) and new_degree < min_degree:
        min_degree_index = move_index
        min_degree = new_degree

    if min_degree_index == -1: return

    new_x = x + self.moves[min_degree_index][0]
    new_y = y + self.moves[min_degree_index][1]
    self.board[new_x][new_y] = self.board[x][y] + 1

    return [new_x, new_y]

  def is_neighbor(self, x1, y1, x2, y2):
    for move in self.moves:
      new_x = x1 + move[0]
      new_y = y1 + move[1]
      if new_x == x2 and new_y == y2: return True
    return False

test_class(Solution2, examples)

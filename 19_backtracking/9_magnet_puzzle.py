from utils import test_class

# The Magnet puzzle involves placing a set of domino-shaped magnets (or electrets or
# other polarized objects) in a subset of slots on a board to satisfy a set of constraints.
# Each slot contains either a blank entry (indicated by x), or a magnet with a positive
# and a negative end.
# The numbers along the left and top sides show the numbers of + squares in those
# particular rows or columns. Those along the right and bottom show the number of - signs
# those particular rows or columns.
# Rows and columns without a number at one or both ends are unconstrained to the number
# of + or - signs, depending on which number is not present.
# In addition to fulfilling these numerical constraints, a puzzle solution must also
# satisfy the constraint that no two orthogonally touching squares may have the same sign
# (diagonally joined squares are not constrained).
# You are given top[], bottom[], left[], right[] arrays indicates the count of + or –
# along the top(+), bottom(-), left(+) and right(-) edges respectively.
# Values of -1 indicate any number of + and – signs.
# Also given matrix rules[][] contain any one T, B, L or R characters.
# For a vertical slot, T indicates its top end and B indicates the bottom end.
# For a horizontal slot, L indicates left end and R indicates the right end.

examples = [
  {
    'input': [
      5, # m
      6, # n
      [1, -1, -1, 2, 1, -1], # top
      [2, -1, -1, 2, -1, 3], # bottom
      [2, 3, -1, -1, -1], # left
      [-1, -1, -1, 1, -1], # right
      [
        ['L', 'R', 'L', 'R', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B'],
        ['T', 'T', 'T', 'T', 'L', 'R'],
        ['B', 'B', 'B', 'B', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B']
      ] # right
    ],
    'output': [
      ['+', '-', '+', '-', 'X', '-'],
      ['-', '+', '-', '+', 'X', '+'],
      ['X', 'X', '+', '-', '+', '-'],
      ['X', 'X', '-', '+', 'X', '+'],
      ['-', '+', 'X', 'X', 'X', '-'],
    ]
  },
  {
    'input': [
      4, # m
      3, # n
      [2, -1, -1], # top
      [-1, -1, 2], # bottom
      [-1, -1, 2, -1], # left
      [0, -1, -1, -1], # right
      [
        ['T', 'T', 'T'],
        ['B', 'B', 'B'],
        ['T', 'L', 'R'],
        ['B', 'L', 'R']
      ], # rules
    ],
    'output': [
      ['+', 'X', '+'],
      ['-', 'X', '-'],
      ['+', '-', '+'],
      ['-', '+', '-'],
    ]
  },
]

# Time Complexity: Exponential
# Auxiliary Space: O(1)
class Solution:
  def solve(self, m, n, top, bottom, left, right, rules):
    self.m = m
    self.n = n
    self.top = top
    self.bottom = bottom
    self.left = left
    self.right = right
    self.rules = rules

    self.patterns = ['+-', '-+', 'XX']

    self.magnets(0, 0)
    return self.rules

  def magnets(self, row, col):
    # If the current row is iterated, go to the next row
    if col >= self.n:
      row += 1
      col = 0

    if row == self.m:
      # print('yes')
      return self.check_constraints()

    if self.rules[row][col] == 'L':
      for pattern in self.patterns:
        if not self.valid_horizontal_pattern(row, col, pattern): continue

        # print(row, col, self.rules[row][col], pattern)
        self.rules[row][col] = pattern[0]
        self.rules[row][col + 1] = pattern[1]

        if self.magnets(row, col + 2): return True

        self.rules[row][col] = 'L'
        self.rules[row][col + 1] = 'R'

      return False

    if self.rules[row][col] == 'T':
      for pattern in self.patterns:
        if not self.valid_vertical_pattern(row, col, pattern): continue

        # print(row, col, self.rules[row][col], pattern)
        self.rules[row][col] = pattern[0]
        self.rules[row + 1][col] = pattern[1]

        if self.magnets(row, col + 1): return True

        self.rules[row][col] = 'T'
        self.rules[row + 1][col] = 'B'

      return False

    return self.magnets(row, col + 1)

  def valid_horizontal_pattern(self, row, col, pattern):
    if pattern == 'XX': return True

    # For example, assume +- is the current pattern
    # + on the left of + is not allowed
    if col - 1 >= 0 and self.rules[row][col - 1] == pattern[0]:
      return False
    # + on the top of + is not allowed
    if row - 1 >= 0 and self.rules[row - 1][col] == pattern[0]:
      return False

    # - on the top of - is not allowed
    if row - 1 >= 0 and self.rules[row - 1][col + 1] == pattern[1]:
      return False
    # # - on the right of - is not allowed
    if col + 2 < self.n and self.rules[row][col + 2] == pattern[1]:
      return False

    return True

  def valid_vertical_pattern(self, row, col, pattern):
    if pattern == 'XX': return True

    # For example, assume +- is the current pattern
    # + on the left of + is not allowed
    if col - 1 >= 0 and self.rules[row][col - 1] == pattern[0]:
      return False
    # + on the top of + is not allowed
    if row - 1 >= 0 and self.rules[row - 1][col] == pattern[0]:
      return False
    # + on the right of + is not allowed
    if col + 1 < self.n and self.rules[row][col + 1] == pattern[0]:
      return False

    return True

  def check_constraints(self):
    row_pos = [0] * self.m
    row_neg = [0] * self.m
    col_pos = [0] * self.n
    col_neg = [0] * self.n

    for row in range(self.m):
      for col in range(self.n):
        charge = self.rules[row][col]
        if charge == '+':
          row_pos[row] += 1
          col_pos[col] += 1
        elif charge == '-':
          row_neg[row] += 1
          col_neg[col] += 1

    for row in range(self.m):
      if self.left[row] != -1:
        if row_pos[row] != self.left[row]:
          return False

      if self.right[row] != -1:
        if row_neg[row] != self.right[row]:
          return False

    for col in range(self.n):
      if self.top[col] != -1:
        if col_pos[col] != self.top[col]:
          return False

      if self.bottom[col] != -1:
        if col_neg[col] != self.bottom[col]:
          return False

    return True

test_class(Solution, examples)

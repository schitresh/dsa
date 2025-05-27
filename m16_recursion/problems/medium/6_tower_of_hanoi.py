from utils import test_class

# Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C)
# and N disks. Initially, all the disks are stacked in decreasing value of diameter
# i.e. the smallest disk is placed on the top and they are on rod A. The objective
# is to move the entire stack to another rod (here considered C), obeying these
# rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the topmost disk from one of the stacks and
# placing it on top of another stack.
# 3. No disk may be placed on top of a smaller disk.
# Given N, output the steps to achieve this as an array of [disk, from, to]

examples = [
  {
    'input': [2],
    'output': [
      [1, 'A', 'B'],
      [2, 'A', 'C'],
      [1, 'B', 'C'],
    ],
  },
  {
    'input': [3],
    'output': [
      [1, 'A', 'C'],
      [2, 'A', 'B'],
      [1, 'C', 'B'],
      [3, 'A', 'C'],
      [1, 'B', 'A'],
      [2, 'B', 'C'],
      [1, 'A', 'C'],
    ],
  },
]

# Recursion
# 1. Shift N-1 disks from A to B using C.
# 2. Shift last disk from A to C.
# 3. Shift N-1 disks from B to C using A.
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n):
    self.moves = []
    self.tower_of_hanoi(n, 'A', 'C', 'B')
    return self.moves

  def tower_of_hanoi(self, n, from_rod, to_rod, aux_rod):
    if n == 0: return

    # Shift N-1 disks from A to B using C
    self.tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    # Shift last disk from A to C
    self.moves.append([n, from_rod, to_rod])
    # Shift N-1 disks from B to C using A
    self.tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

test_class(Solution, examples)

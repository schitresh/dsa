from utils import test_class

# Given n rectangular buildings in a 2-dimensional city, computes the skyline of these
# buildings, eliminating hidden lines. The main task is to view buildings from a side and
# remove all sections that are not visible. All buildings share a common bottom and every
# building is represented by a triplet (left, ht, right)
# 'left' is the x coordinate of the left side (or wall)
# 'ht' is the height of the building
# 'right' is x coordinate of the right side
# A skyline is a collection of rectangular strips. A rectangular strip is represented as
# a pair (left, ht) where left is x coordinate of the left side of the strip and ht is the
# height of the strip.

examples = [
  {
    'input': [[[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25],
              [19, 18, 22], [23, 13, 29], [24, 4, 28]]],
    'output': [[1, 11], [3, 13], [9, 0], [12, 7], [16, 3],
              [19, 18], [22, 3], [23, 13], [29, 0]],
  },
  {
    'input': [[[1, 11, 5]]],
    'output': [[1, 11], [5, 0]],
  },
]

# Todo
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, buildings):
    return

test_class(Solution, examples)

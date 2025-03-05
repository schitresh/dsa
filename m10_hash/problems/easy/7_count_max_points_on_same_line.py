from math import gcd
from utils import test_class

# Given N point on a 2D plane as pair of (x, y) co-ordinates, find the maximum number of
# point which lie on the same line.

examples = [
  {
    'input': [[[-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [3, 4]]],
    'output': 4,
    # [0, 0], [1, 1], [2, 2], [3, 3]
  },
]

# Hashing
# For any two points (x1, y1) and (x2, y2), their slope should be equal to be on the
# same line. Slope for these two points is rise/run, i.e (y2 – y1) / (x2 – x1), which
# can be a double value and can cause precision problems. To get rid of the precision
# problems, treat the slope as pair ((y2 – y1), (x2 – x1)) instead of ratio and reduce
# the pair by their gcd before inserting into map.
# Time Complexity: O(n^2 * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    max_points = 0

    for i in range(len(array) - 1):
      slope_points = {}

      for j in range(i + 1, len(array)):
        # List is not hashable, so use tuple
        slope = tuple(self.normalized_slope(array[i], array[j]))

        if slope in slope_points: slope_points[slope] += 1
        else: slope_points[slope] = 2 # Need to count both i & j initially

      curr_max = max(slope_points.values())
      max_points = max(max_points, curr_max)

    return max_points

  def normalized_slope(self, point1, point2):
    run = point2[0] - point1[0]

    # Normalize undefined slopes to [1, 0]
    if run == 0: return [1, 0]

    # Normalize to left to right
    if run < 0:
      point1, point2 = point2, point1
      run = point2[0] - point1[0]

    rise = point2[1] - point1[1]
    gcd_val = gcd(abs(rise), run)
    return [rise // gcd_val, run // gcd_val]

test_class(Solution, examples)

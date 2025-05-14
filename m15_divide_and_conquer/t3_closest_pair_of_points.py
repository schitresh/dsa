import math
from utils import test_class

# Given an array of n distinct points in a 2D plane, find the closest pair of points

examples = [
  {
    'input': [[[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]],
    'output': 1.41421,
  },
  {
    'input': [[[-2, -2], [1, 2], [-1, 0], [3, 3]]],
    'output': 2.23607,
  }
]

# Brute Force
# Compute distance between all the pairs of the points
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

# Divide & Conquer
# 1. Sort the points by x coordinate. This allows us to divide the points into two halves
# on x axis.
# 2. Calculate the min distance in each half. Consider the pairs that have one point in the
# left half and the other in the right half.
# 3. Consider only those points whose distance from the mid y-line is less than the current
# min distance. Sort these points according to y coordinates.
# 4. Find the min distance in this strip and compare with the current min distance.
# Time Complexity: O(n * log(n)^2)
# Auxiliary Space: O(log(n))
class Solution:
  def solve(self, points):
    points.sort(key = lambda p: p[0])
    min_dist = self.closest_pair(points, 0, len(points) - 1)
    return round(min_dist, ndigits = 5)

  def closest_pair(self, points, left, right):
    # Compare two pairs using 3 points, avoid divide & conquer overhead, brute force is
    # more efficient for two pairs
    if right - left <= 2:
      return self.brute_force_min(points, left, right)

    mid = left + (right - left) // 2
    left_min = self.closest_pair(points, left, mid)
    right_min = self.closest_pair(points, mid + 1, right)
    min_dist = min(left_min, right_min)

    strip = []
    for i in range(left, right):
      if abs(points[i][0] - points[mid][0]) < min_dist:
        strip.append(points[i])

    min_dist_strip = self.closest_pair_in_strip(strip, min_dist)
    return min(min_dist, min_dist_strip)

  def brute_force_min(self, points, left, right):
    min_dist = float('inf')

    for i in range(left, right):
      for j in range(left + 1, right):
        dist = self.dist(points[i], points[j])
        min_dist = min(min_dist, dist)

    return min_dist

  # distance = sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
  def dist(self, point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

  def closest_pair_in_strip(self, strip, min_dist):
    strip.sort(key = lambda p: p[1])

    for i in range(len(strip)):
      for j in range(i + 1, len(strip)):
        if strip[j][1] - strip[i][1] >= min_dist:
          break

        dist = self.dist(strip[i], strip[j])
        min_dist = min(min_dist, dist)

    return min_dist

test_class(Solution, examples)

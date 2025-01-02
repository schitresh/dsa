import math
from utils import test_class

# Given an array of n points in a plane, find the closest pair of points.

examples = [
  {
    'input': [[[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]],
    'output': 1.41421
  }
]

# Brute Force: Compute distance between each pair
# Time Complexity: O(n^2)

# Sort the points according to x coordinates. This allows us to divide the points into
# two halves on x axis, and calculate min distance in each half.
# Consider the pairs that have one point in left half and the other in right half.
# Consider only those points whose distance from the mid y-line is less than the current
# min distance. Sort these points according to y coordinates.
# Find min distance in these points and compare with the current min distance
# Time Complexity: O(n * log(n)^2)
# Auxiliary Space: O(log(n))
class Solution:
  def dist(self, point1, point2):
    # distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

  def closest_pair_in_strip(self, strip, min_dist):
    strip = sorted(strip, key = lambda x: x[1])

    for i in range(len(strip)):
      for j in range(i + 1, len(strip)):
        if strip[j][1] - strip[i][1] > min_dist:
          break

        dist = self.dist(strip[i], strip[j])
        min_dist = min(min_dist, dist)

    return min_dist

  def closest_pair(self, points, left, right):
    if left >= right:
      return float('inf')

    if left + 1 == right:
      return self.dist(points[left], points[right])

    mid = left + (right - left) // 2
    left_min = self.closest_pair(points, left, mid)
    right_min = self.closest_pair(points, mid + 1, right)
    min_dist = min(left_min, right_min)

    strip = []
    for i in range(left, right + 1):
      if abs(points[i][0] - points[mid][0]) < min_dist:
        strip.append(points[i])

    min_dist_strip = self.closest_pair_in_strip(strip, min_dist)
    return min(min_dist, min_dist_strip)

  def solve(self, points):
    points = sorted(points, key = lambda x: x[0])
    min_dist = self.closest_pair(points, 0, len(points) - 1)
    return round(min_dist, ndigits = 5)

test_class(Solution, examples)

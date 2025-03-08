from heapq import heapify, heappush
from utils import test_class

# Given n rectangular buildings in a 2-dimensional city, compute the skyline of these
# buildings, eliminating hidden lines.
# The main task is to view buildings from a side and remove all sections that are not
# visible. All buildings share a common bottom and each building is represented by a
# triplet (left, ht, right) where:
# 'left' is the x coordinate of the left side (or wall)
# 'ht' is the height of the building
# 'right' is x coordinate of the right side

# A skyline is a collection of rectangular strips. A rectangular strip is represented as
# a pair (x, ht) where x is the x coordinate and ht is the height of the strip.
# For the left side it will be (left, ht) and for the right side it will be (right, 0).
# But if there is another building present ahead of the right side, then it will be
# (right, height of the building ahead).

examples = [
  {
    'input': [[
      [1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22],
      [23, 13, 29], [24, 4, 28]
    ]],
    'output': [
      [1, 11], [3, 13], [9, 0], [12, 7], [16, 3], [19, 18], [22, 3], [23, 13],
      [29, 0]
    ],
  },
  {
    'input': [[[1, 11, 5]]],
    'output': [[1, 11], [5, 0]],
  },
]

# Divide and Conquer
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, buildings):
    return self.skyline(buildings, 0, len(buildings) - 1)

  def skyline(self, buildings, left, right):
    if left == right:
      building = buildings[left]
      return [[building[0], building[1]], [building[2], 0]]

    mid = (left + right) // 2
    left_skyline = self.skyline(buildings, left, mid)
    right_skyline = self.skyline(buildings, mid + 1, right)
    return self.merge_skylines(left_skyline, right_skyline)

  def merge_skylines(self, left, right):
    skyline = []
    i = 0
    j = 0
    height_left = 0
    height_right = 0

    while i < len(left) and j < len(right):
      if left[i][0] < right[j][0]:
        x_coord, height_left = left[i]
        i += 1
      else:
        x_coord, height_right = right[j]
        j += 1

      # Need to track both left and right height because left and right buildings
      # may overlap. And we need only the max overlapping height, so keeping a
      # global max height not correct since it the global max height can be anywhere.
      max_height = max(height_left, height_right)

      # If there is no change in height, then it is not a critical point
      if skyline and skyline[-1][1] == max_height:
        continue

      # If the x coordinate is same as the previous point, no need to add it. But it
      # means that the height is different, hence assign maximum height.
      if skyline and skyline[-1][0] == x_coord:
        skyline[-1][1] = max(skyline[-1][1], max_height)
        continue

      skyline.append([x_coord, max_height])

    skyline.extend(left[i:])
    skyline.extend(right[j:])
    return skyline

test_class(Solution, examples)

# Using Heap
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, buildings):
    skyline = []
    # Stores all the critical points (start and end of buildings)
    points = []

    for left, height, right in buildings:
      # Keep height for the start of a building negative to indicate that the
      # building is starting.
      points.append((left, -height))
      # Keep height for the end of a building positive to indicate that the
      # building is ending.
      points.append((right, height))

    # Sort points by x-coordinate and height
    # Since starting points have negative height, they will appear before ending points
    # if they have the same x-coordinates
    points.sort()

    # Max-heap to keep track of building heights in descending order
    # heapq is a min heap, but we will store the heights from the start point only
    # which have negative heights, it will behave as max-heap
    # Initialize with a dummy building of height 0
    heap = [0]
    prev_height = 0

    for x_coord, height in points:
      # If it's the start of a building, add its height to the heap
      if height < 0:
        heappush(heap, height)
      # If it's the end of a building, remove it from the heap
      else:
        heap.remove(-height)
        heapify(heap)

      max_height = -heap[0]
      # If the maximum height has changed, add the current point to the skyline
      if max_height != prev_height:
        skyline.append([x_coord, max_height])
        prev_height = max_height

    return skyline

test_class(Solution2, examples)

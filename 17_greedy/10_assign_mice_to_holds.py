from utils import test_class

# There are N Mice and N holes placed in a straight line. Each hole can accommodate only
# one mouse. A mouse can stay at his position, move one step right from x to x + 1, or
# move one step left from x to x -1. Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets inside a hole is
# minimized.

examples = [
  {
    'input': [[4, -4, 2], [4, 0, 5]], # [positions of mice, positions of holes]
    'output': 4
    # Assign m4 to h4 (0 mins), m(-4) to h0 (4 mins), m2 to h5 (3 mins)
  },
  {
    'input': [[-10, -79, -79, 67, 93, -85, -28, -94], [-2, 9, 69, 25, -31, 23, 50, 78]],
    'output': 102
  },
]

# Greedy approach: Put every mouse to its nearest hold.
# Sort the positions of mice and holes to achieve this.
# This works since we need to minimize the last mouse, and that will be achieved when
# every mouse goes to the nearest hole possible.
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, mouses, holes):
    if len(mouses) != len(holes): return -1
    mouses.sort()
    holes.sort()

    last_mouse_time = 0
    for i in range(len(mouses)):
      curr_time = abs(mouses[i] - holes[i])
      last_mouse_time = max(last_mouse_time, curr_time)

    return last_mouse_time

test_class(Solution, examples)

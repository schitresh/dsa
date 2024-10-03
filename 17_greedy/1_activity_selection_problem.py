from queue import PriorityQueue
from utils import test_class

# Given n activities with their start and finish time,
# select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time

# input: Array of activities with [start_time, finish_time]
examples = [
  {
    'input': [[[10, 20], [12, 25], [20, 30]]],
    'output': [[10, 20], [20, 30]]
  },
  {
    'input': [[[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]],
    'output': [[1, 2], [3, 4], [5, 7], [8, 9]]
  }
]

# The greedy choice is to always pick the next activity
# whose finish time is the least among the remaining activities
# and the start time is more than or equal to the finish time of the previous activity
# We can sort the activities according to their finishing time for easy selection
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, activity_times):
    activity_times.sort(key = lambda x: x[1])
    activities = []

    # Select the first activity to begin
    curr_activity = activity_times[0]
    activities.append(curr_activity)

    for i in range(1, len(activity_times)):
      next_activity = activity_times[i]

      if curr_activity[1] <= next_activity[0]:
        curr_activity = next_activity
        activities.append(curr_activity)

    return activities

test_class(Solution, examples)

# We can use min heap to get the activity with minimum finish tme
# Min heap can be implemented using priority queue
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, activity_times):
    activity_times.sort(key = lambda x: x[1])
    activities = []

    heap = PriorityQueue()
    for activity in activity_times:
      heap.put([activity[1], activity[0]])

    item = heap.get()
    curr_activity = [item[1], item[0]]
    activities.append(curr_activity)

    while not heap.empty():
      item = heap.get()
      next_activity = [item[1], item[0]]

      if curr_activity[1] <= next_activity[0]:
        curr_activity = next_activity
        activities.append(curr_activity)

    return activities

test_class(Solution2, examples)

import heapq
from utils import test_class

# Given an array of jobs where each job has a deadline and associated profit if the job
# is finished before the deadline. Each job takes a single unit of time to finish.
# Maximize the total profit if only one job can be scheduled at a time.

examples = [
  {
    'input': [[
      ['a', 2, 100],
      ['b', 1, 19],
      ['c', 2, 27],
      ['d', 1, 25],
      ['e', 3, 15]
    ]], # [name, deadline, profit]
    'output': ['c', 'a', 'e'],
  },
]

# Greedily choose the job with the maximum profit first by sorting the jobs in
# decreasing order of their profit
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, jobs):
    jobs.sort(key = lambda x: x[2], reverse = True)

    max_deadline = max(jobs, key = lambda x: x[1])[1]
    time_slots = [None] * max_deadline

    for job in jobs:
      deadline_slot = job[1] - 1

      for slot in range(deadline_slot, -1, -1):
        if not time_slots[slot]:
          time_slots[slot] = job[0]
          break

    return time_slots

test_class(Solution, examples)

# Sort the jobs in decreasing order of their deadlines and then calculate the available
# slots between every consecutive deadlines.
# Include the profit of the job at the root of the max heap while the empty slots are
# available and heap is not empty. This will help to choose the jobs with maximum profit
# for every set of available slots.
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, jobs):
    jobs.sort(key = lambda x: x[1], reverse = True)

    selected_jobs = []
    max_heap = []

    for i in range(len(jobs)):
      deadline = jobs[i][1]
      slots_available = deadline

      if i + 1 < len(jobs):
        next_deadline = jobs[i + 1][1]
        slots_available = deadline - next_deadline

      # Keep the job with the max profit at the top
      # If there are multiple jobs with the same deadline, slots_available will be 0
      # and this will keep the job with max profit at the top
      # We push negative value for max heap in python (positive value will give min heap)
      heapq.heappush(max_heap, [-jobs[i][2], jobs[i][1], jobs[i][0]])

      while slots_available and max_heap:
        _job_profit, job_deadline, job_id = heapq.heappop(max_heap)
        slots_available -= 1
        selected_jobs.append([job_id, job_deadline])

    selected_jobs.sort(key = lambda x: x[1])

    return list(map(lambda x: x[0], selected_jobs))

test_class(Solution2, examples)

from utils import test_class

# Given N machines, each machine contains some numbers in sorted form. But the amount of
# numbers each machine has is not fixed. Sort the numbers from all the machine in
# non-decreasing order.

examples = [
  {
    'input': [[[30, 40, 50], [35, 45], [10, 60, 70, 80, 100]]],
    'output': [10, 30, 35, 40, 45, 50, 60, 70, 80, 100],
  },
]

# Track indexes for each machine and selectively add the minimum number
# Time Complexity: O(n * max_len_of_machine)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, machines):
    result = []
    indexes = [0] * len(machines)

    while True:
      min_num = float('inf')
      for i in range(len(machines)):
        if indexes[i] < len(machines[i]):
          num = machines[i][indexes[i]]
          min_num = min(min_num, num)

      if min_num == float('inf'): break

      for i in range(len(machines)):
        if indexes[i] < len(machines[i]):
          num = machines[i][indexes[i]]
          if num == min_num:
            result.append(num)
            indexes[i] += 1

    return result

test_class(Solution, examples)

# Todo: Using Priority Queue
# Time Complexity: O(total_nums * log(n))
# Auxiliary Space: O(total_nums)
class Solution2:
  def solve(self, machines):
    result = []
    return result

test_class(Solution2, examples)

from utils import test_class

# Given a wall of length w and shelves of two lengths m and n
# Find the number of each type of shelf that can be used
# and the remaining empty space such that the empty space is minimum
# The larger of the two shelves is cheaper so it is preferred
# However cost is secondary and the first priority is to minimize empty space on wall

examples = [
  {
    'input': [24, 3, 5], # w, m, n
    'output': [3, 3, 0] # count of m, count of n, empty space
    # [8, 0, 0] can be another solution
    # But since n is larger & hence cheaper, the first answer is preferred
  },
  {
    'input': [29, 3, 9],
    'output': [0, 3, 2]
  },
  {
    'input': [24, 4, 7],
    'output': [6, 0, 0]
  },
]

# Greedy approach: Increase the number of larger shelves till they can fit
# Then increase the number of small shelves till they can fit
# Time Complexity: O(w / max(m, n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, wall, len_m, len_n):
    curr_m = wall // len_m
    curr_n = 0
    curr_empty = wall % len_m

    count_m = curr_m
    count_n = curr_n
    empty = curr_empty

    while wall >= len_n:
      curr_n += 1
      wall -= len_n

      curr_m = wall // len_m
      curr_empty = wall % len_m

      # If empty space is equal, prefer n since it's larger
      if curr_empty <= empty:
        count_m = curr_m
        count_n = curr_n
        empty = curr_empty

    return [count_m, count_n, empty]



test_class(Solution, examples)

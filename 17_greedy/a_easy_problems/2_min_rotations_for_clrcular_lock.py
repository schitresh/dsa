from utils import test_class

# You are given a lock which is made up of n-different circular rings and each ring has
# 0-9 digit printed serially on it. Initially all n-rings together show a n-digit integer
# but there is particular code only which can open the lock. You can rotate each ring any
# number of time in either direction. You have to find the minimum number of rotation done
# on rings of lock to open the lock.

examples = [
  {
    'input': ['2345', '5432'], # Initial code, Unlock code
    'output': 8,
    # 1st ring: 3 (2 to 5), 2nd ring: 1 (3 to 4)
    # 3rd ring: 1 (4 to 3), 4th ring: 3 (5 to 2)
  },
  {
    'input': ['1919', '0000'],
    'output': 4
  }
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, input_code, unlock_code):
    rotations = 0

    for i in range(len(input_code)):
      input_digit = int(input_code[i])
      unlock_digit = int(unlock_code[i])

      diff = abs(unlock_digit - input_digit)
      if diff > 5: diff = 10 - diff

      rotations += diff

    return rotations

test_class(Solution, examples)

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, input_code, unlock_code):
    rotations = 0

    for i in range(len(input_code)):
      input_digit = int(input_code[i])
      unlock_digit = int(unlock_code[i])

      diff1 = abs(unlock_digit - input_digit)
      diff2 = 10 - diff1

      rotations += min(diff1, diff2)

    return rotations

test_class(Solution, examples)

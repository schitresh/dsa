from collections import defaultdict
from utils import test_class

# Given three stacks of the positive numbers, find the possible equal maximum sum of the
# stacks with the removal of top elements allowed. Stacks are represented as an array,
# and the first index of the array represent the top element of the stack.

examples = [
  {
    'input': [[4, 2, 3], [1, 1, 2, 3], [1, 4]],
    'output': 5,
    # Pop 1 element from the 1st stack and 2 elements from the 2nd stack
    # The remaining elements in all the stacks yield the equal sum, that is 5.
  },
  {
    'input': [[3, 10], [4, 5], [2, 1]],
    'output': 0,
  },
  {
    'input': [[3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]],
    'output': 5,
  }
]

# Time Complexity: O(n1 + n2 + n3)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, stack1, stack2, stack3):
    sum1, sum2, sum3 = sum(stack1), sum(stack2), sum(stack3)
    idx1 = idx2 = idx3 = 0

    if sum1 == sum2 and sum2 == sum3: return sum1

    while idx1 < len(stack1) and idx2 < len(stack2) and idx3 < len(stack3):
      if sum1 > sum2 and sum1 > sum3:
        sum1 -= stack1[idx1]
        idx1 += 1
      elif sum2 > sum1 and sum2 > sum3:
        sum2 -= stack2[idx2]
        idx2 += 1
      elif sum3 > sum1 and sum3 > sum2:
        sum3 -= stack3[idx3]
        idx3 += 1

      if sum1 == sum2 and sum2 == sum3:
        return sum1

    return 0

test_class(Solution, examples)

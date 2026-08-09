from utils import test_class

# Convert the given decimal number into an equivalent binary number.

examples = [
  {
    'input': [7],
    'output': '111'
  },
  {
    'input': [10],
    'output': '1010'
  },
    {
    'input': [1024],
    'output': '10000000000'
  },
]

# Time Complexity: O(log2(n))
# Auxiliary Space: O(log2(n)), due to recursive stack
class Solution:
  def solve(self, num):
    if num < 2: return str(num)

    binary_digit = num % 2
    return self.solve(num // 2) + str(binary_digit)

test_class(Solution, examples)

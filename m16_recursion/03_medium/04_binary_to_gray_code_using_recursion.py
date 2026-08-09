from utils import test_class

# Given the binary code of a number as a decimal number, convert it into its
# equivalent gray code. Assume that the binary number is in the range of integers.
# For the larger value, we can take a binary number as string.
# In gray code, consecutive numbers differ by only one bit. The most significant
# bit is equal to the MSB of the binary code. Other bits can be obtained by the XOR
# of the bit and its previous bit.

examples = [
  {
    'input': [1001],
    'output': 1101,
  },
  {
    'input': [11001],
    'output': 10101,
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, binary_code):
    if binary_code // 10 == 0: return binary_code

    bit = binary_code % 10
    prev_bit = (binary_code // 10) % 10
    gray_bit = prev_bit ^ bit
    return self.solve(binary_code // 10) * 10 + gray_bit

test_class(Solution, examples)

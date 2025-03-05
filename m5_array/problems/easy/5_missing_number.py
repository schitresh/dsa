from utils import test_class

# Given an array of size n-1 with distinct integers in the range [1, n]. This array
# represents a permutation of the integers from 1 to n with one element missing. Find
# the missing element in the array.

examples = [
  {
    'input': [[1, 2, 4, 6, 3, 7, 8]],
    'output': 5,
  },
  {
    'input': [[1, 2, 3, 5]],
    'output': 4,
  },
]

# Naive Approach
# Iterate over array for numbers 1 to n to check if it exists or not

# Hash Approach
# Keep track of the numbers occurred by using array as hash
# The indexes from 1 to n which will have 0 or false is the missing number

# Sum of n terms
# Sum of first n natural numbers is n * (n + 1) / 2
# Subtract the sum of array from this to get the missing number
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    n = len(array) + 1
    sum_n = n * (n + 1) // 2
    return sum_n - sum(array)

test_class(Solution, examples)

# Using XOR
# XOR of a number with itself is 0. Hence, XOR of the numbers from 0 to n with XOR of the
# numbers in the array should give the missing number.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    xor_n = 0
    xor_array = 0

    # n = len(array) + 1 since a number is missing
    for i in range(1, len(array) + 2):
      xor_n ^= i

    for item in array:
      xor_array ^= item

    return xor_n ^ xor_array

test_class(Solution2, examples)

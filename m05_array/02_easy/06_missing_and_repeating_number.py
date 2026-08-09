from utils import test_class

# Given an unsorted array of size n where elements are in the range of 1 to n. One
# number from the set (1, 2, ..., n) is missing and one number occurs twice in the
# array. Find the missing & the repeating numbers.

examples = [
  {
    'input': [[3, 1, 3]],
    'output': [2, 3],
  },
  {
    'input': [[4, 3, 6, 2, 1, 1]],
    'output': [5, 1],
  },
  {
    'input': [[4, 3, 6, 2, 1, 6, 7]],
    'output': [5, 6],
  },
]

# Naive Approach
# Iterate over array for numbers 1 to n to check if it exists or repeating

# Hash Approach
# Keep track of the numbers occurred by using array as hash
# The indexes from 1 to n which will have 0 or false is the missing number
# And the one which already has 1 or true is the repeating number

# Track visited using indexes & negation
# Calculate the sum of the first n natural numbers. In the array, use every element as
# an index. Make the value at this index negative to mark the element visited. If the
# element has already been visited, then this is the repeating number.
# Also, if this element was not visited before, subtract it from S(n), i.e. the sum of
# first n natural numbers. This will give us the missing number since we've already
# avoided the repeating number.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    n = len(array)
    missing = (n * (n + 1)) // 2
    repeating = 0

    for i in range(len(array)):
      index = abs(array[i]) - 1

      if array[index] > 0:
        array[index] *= -1
        missing -= abs(array[i])
      else:
        repeating = abs(array[i])

    return [missing, repeating]

test_class(Solution, examples)

# Sum of n terms
# Let x be the missing and y be the repeating element
# Sum of first n natural numbers is S(n) = n * (n + 1) / 2
# Hence, S(n) = S(array) + x - y
# Sum of squares of first n natural numbers is S(n^2) = n * (n + 1) * (2n + 1) / 6
# Hence, S(n^2) = S(array^2) + x^2 - y^2
# From these equations (keeping in mind that x^2 - y^2 = (x + y) * (x - y)),
# x - y = S(n) - S(array) = A
# x + y = [S(array^2) - S(n^2)] / A = B / A
# That is, x = (A + B/A) / 2 and y = x - A
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    n = len(array)
    sum_n = n * (n + 1) // 2
    sum_n_sq = n * (n + 1) * (2 * n + 1) // 6

    # Subtract using loop since we'll have to loop anyways to find sum of squares
    diff_a = sum_n
    diff_b = sum_n_sq
    for item in array:
      diff_a -= item
      diff_b -= item * item

    missing = (diff_a + (diff_b // diff_a)) // 2
    repeating = missing - diff_a
    return [missing, repeating]

test_class(Solution2, examples)

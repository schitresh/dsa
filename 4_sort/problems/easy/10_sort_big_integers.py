from utils import test_class

# Given an array of positive integers where each integer can have digits upto 10^6,
# sort the array elements in ascending order.

examples = [
  {
    'input': [[54, 724523015759812365462, 870112101220845, 8723]],
    'output': [54, 8723, 870112101220845, 724523015759812365462],
  },
  {
    'input': [[4510122010112121012121, 3641264874311, 451234654453211101231]],
    'output': [3641264874311, 451234654453211101231, 4510122010112121012121],
  },
]

# Naive approach
# Use arbitrary precision data type such as int in python or Biginteger class in Java.
# But that approach will not be fruitful because internal conversion of string to int
# and then perform sorting will slow down the calculations of addition and
# multiplications in binary number system.

# Convert to String
# If lengths of two strings are different, compare the lengths to decide sorting order.
# Else compare both the strings in lexicographically order.
# Time Complexity: O(sum_string_lens * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    array = list(map(str, array))
    array.sort(key = lambda x: (len(x), x))
    array = list(map(int, array))
    return array

test_class(Solution, examples)

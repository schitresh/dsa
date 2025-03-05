import math
from utils import test_class

# Egyptian Fraction
# Every positive fraction can be represented as sum of unique unit fractions.
# A fraction is unit fraction if numerator is 1 and denominator is a positive integer.
# For example, 1/3 is a unit fraction.

examples = [
  {
    'input': ['2/3'],
    'output': ['1/2', '1/6']
  },
  {
    'input': ['6/14'],
    'output': ['1/3', '1/11', '1/231']
  },
  {
    'input': ['12/13'],
    'output': ['1/2', '1/3', '1/12', '1/156']
  },
]

# We can generate Egyptian Fractions using Greedy Algorithm
# For a given number of the form nr/dr where nr < dr, find the greatest possible unit
# fraction and then recur for the remaining part.
# For example, consider 6/14, we first find ceiling of 14/6, i.e. 3.
# So the first unit fraction becomes 1/3, then recur for (6/14 – 1/3) i.e. 4/42.
# Time Complexity: O(d), where d is the denominator of the input fraction
# Auxiliary Space: O(1)
class Solution:
  def solve(self, fraction):
    nr, dr = map(int, fraction.split('/'))
    denominators = []

    while nr != 0:
      curr_egy_dr = math.ceil(dr / nr)
      denominators.append(curr_egy_dr)

      nr = nr * curr_egy_dr - dr
      dr = dr * curr_egy_dr

    return list(map(lambda x: f'1/{x}', denominators))

test_class(Solution, examples)

from utils import test_class

# Given an integer n, find the total number of unique BSTs that can be made using the
# values from 1 to n.

examples = [
  {
    'input': [3],
    'output': 5,
    # Preorder traversals: [1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]
  },
  {
    'input': [2],
    'output': 2,
    # Preorder traversals: [1, 2], [2, 1]
  },
]

# Each of the n nodes can serve as the root.
# For any selected root, the remaining nodes must be divided into two groups. Nodes with
# keys smaller than the root key and nodes with keys larger than the root key.
# Since the left & the right subtrees are contructed independently, we can multiply these
# counts to get the total number of BSTs for the current configuration, i.e.
# C(i) = C(i - 1) * C(n - i).
# To find the total number of BSTs with n nodes, sum this product across all possible
# roots, C(n) = Sum(i = 1 to n)[C(i - 1) * C(n - i)].
# This formula corresponds to the nth Catalan number.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, n):
    coeff = self.binomial_coeff(2 * n, n)
    return coeff // (n + 1)

  def binomial_coeff(self, n, r):
    result = 1

    # C(n, r) = C(n, n - r) because C(n, r) = n!/(r! * (n - r)!)
    r = min(r, n - r)

    # On expanding the factorials in the formula, it can be simplified to:
    # C(n, r) = (n/1) * ((n-1)/2) * ... * ((n - (r - 1))/r)
    for i in range(r):
      result *= (n - i)
      result //= (i + 1)

    return result

test_class(Solution, examples)

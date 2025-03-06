from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary search tree and a positive integer k, find the kth largest element
# in the BST.

examples = [
  {
    'input': [3, binary_tree_from_level_array([
      [20], [[8, 22]], [[4, 12], None], [None, [10, 14]]]
    )],
    'output': 14,
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(height)
class Solution:
  def solve(self, k, tree):
    self.k = k
    self.count = 0
    self.val = 0
    self.k_largest(tree.root)
    return self.val

  def k_largest(self, node):
    if not node: return

    self.k_largest(node.right)

    self.count += 1

    if self.count == self.k:
      self.val = node.key
      return

    self.k_largest(node.left)

test_class(Solution, examples)

# Todo: Reverse Morris Traversal
# Time Complexity: O(n)
# Auxiliary Space: O(height)

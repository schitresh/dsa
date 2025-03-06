from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, determine if it is height-balanced. A binary tree is considered
# height-balanced if the absolute difference in heights of the left and right subtrees
# is at most 1 for every node in the tree.

examples = [
  {
    'input': [binary_tree_from_level_array([[1], [[2, 3]], [[4, 6], None]])],
    'output': True
  },
  {
    'input': [binary_tree_from_level_array([
      [1], [[2, 3]], [[4, None], None], [[5, None]]]
    )],
    'output': False,
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, tree):
    bal = self.is_balanced(tree.root)
    if bal == -1: return False
    return True

  def is_balanced(self, node):
    if not node: return 0

    left_nodes = self.is_balanced(node.left)
    right_nodes = self.is_balanced(node.right)

    if left_nodes == -1 or right_nodes == -1: return -1
    if abs(left_nodes - right_nodes) > 1: return -1
    return 1 + max(left_nodes, right_nodes)

test_class(Solution, examples)

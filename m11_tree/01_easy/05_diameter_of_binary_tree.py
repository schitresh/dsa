from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, determine the diameter of the tree. The diameter or width of a
# tree is defined as the number of edges on the longest path between any two nodes.

examples = [
  {
    'input': [binary_tree_from_level_array([[1], [[2, 3]]])],
    'output': 2
    # The longest path has 2 edges (2 -> 1 -> 3)
  },
  {
    'input': [binary_tree_from_level_array([[5], [[8, 6]], [[3, 7], [9, None]]])],
    'output': 4,
    # The longest path has 4 edges (3 -> 8 -> 5 -> 6 -> 9).
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(height)
class Solution:
  def solve(self, tree):
    self.diameter = -1
    self.cal_diameter(tree.root)
    return self.diameter

  def cal_diameter(self, node):
    if not node: return -1

    left_height = 1 + self.cal_diameter(node.left)
    right_height = 1 + self.cal_diameter(node.right)
    curr_diameter = left_height + right_height
    self.diameter = max(self.diameter, curr_diameter)

    return max(left_height, right_height)

test_class(Solution, examples)

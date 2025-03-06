from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# In a binary tree, inorder successor of a node is the next node in the inorder
# traversal. Inorder successor is NULL for the last node in inorder traversal.

examples = [
  {
    'input': [8, binary_tree_from_level_array([
      [20], [[8, 22]], [[4, 12], None], [None, [10, 14]]]
    )],
    'output': 10,
  },
  {
    'input': [10, binary_tree_from_level_array([
      [20], [[8, 22]], [[4, 12], None], [None, [10, 14]]]
    )],
    'output': 12,
  },
  {
    'input': [14, binary_tree_from_level_array([
      [20], [[8, 22]], [[4, 12], None], [None, [10, 14]]]
    )],
    'output': 20,
  },
]

# Recursive Inorder Traversal
# Keep track of whether the target has been reached or not. If the target has reached,
# return the key from the next inorder node.
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, target, tree):
    self.target = target
    self.target_accessed = False
    return self.inorder_traversal(tree.root)

  def inorder_traversal(self, node):
    if not node: return None

    successor = self.inorder_traversal(node.left)
    if successor: return successor

    if self.target_accessed:
      return node.key

    if node.key == self.target:
      self.target_accessed = True

    return self.inorder_traversal(node.right)

test_class(Solution, examples)

# BST Search
# Follow the idea of normal BST search. In BST search, we get closer to the key by
# comparing with the current node. So the last greater key visited during search is the
# successor. The following cases arise during the search:
# 1. If the current node is greater, then it is a potential successor. Mark it as
# successor and proceed to left
# 2. If the current node is smaller or equal to the target, proceed to right.
# Time Complexity: O(height)
# Space Complexity: O(1)
class Solution2:
  def solve(self, target, tree):
    successor = None
    temp = tree.root

    while temp:
      if target < temp.key:
        successor = temp.key
        temp = temp.left
      else:
        temp = temp.right

    return successor

test_class(Solution2, examples)

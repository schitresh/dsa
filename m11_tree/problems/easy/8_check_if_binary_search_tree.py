from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, check whether it is a binary search tree or not.
# A Binary Search Tree (BST) is a binary tree with the following properties:
# 1. All keys in the left subtree are smaller than the root and all keys in the right
# subtree are greater.
# 2. Both the left and the right subtrees must also be binary search trees.
# 3. Each key must be distinct.

examples = [
  {
    'input': [binary_tree_from_level_array([[2], [[1, 3]], [None, [None, 5]]])],
    'output': True
  },
  {
    'input': [binary_tree_from_level_array([
      [2], [[1, 7]], [None, [None, 6]], [[None, 9]]
    ])],
    'output': False,
  },
  {
    'input': [binary_tree_from_level_array([[10], [[5, 20]], [None, [9, 25]]])],
    'output': False
  },
]

# Recursive DFS with range of min & max values
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, tree):
    return self.is_bst(tree.root, -float('inf'), float('inf'))

  def is_bst(self, node, min_limit, max_limit):
    if not node: return True
    if node.key <= min_limit or node.key >= max_limit: return False

    left_bst = self.is_bst(node.left, min_limit, node.key)
    right_bst = self.is_bst(node.right, node.key, max_limit)
    return left_bst and right_bst

test_class(Solution, examples)

# Inorder Traversal
# Inorder traversal is left -> node -> right. For BST, inorder traversal will output
# values in sorted order since for each node: left_subtree < node < right_subtree.
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution2:
  def solve(self, tree):
    return self.is_bst(tree.root, [float('-inf')])

  def is_bst(self, node, prev):
    if not node: return True

    if not self.is_bst(node.left, prev): return False

    # Array used for pass by reference to keep a global value
    if prev[0] >= node.key: return False
    prev[0] = node.key

    return self.is_bst(node.right, prev)

test_class(Solution2, examples)

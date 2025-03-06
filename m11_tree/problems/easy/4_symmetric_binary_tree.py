from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, convert the binary tree to its mirror tree. Mirror of a binary
# tree is another binary tree with left and right children of all non-leaf nodes
# interchanged.

examples = [
  {
    'input': [
      binary_tree_from_level_array([[1], [2, 2], [[3, 4], [4, 3]]]),
    ],
    'output': True,
  },
  {
    'input': [
      binary_tree_from_level_array([[1], [2, 2], [[None, 3], [None, 3]]]),
    ],
    'output': False,
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(log(n)), where height = log(n)
class Solution:
  def solve(self, tree):
    self.mirror_tree(tree.root)
    return tree.level_order()

  def mirror_tree(self, node):
    if not node: return

    node.left, node.right = node.right, node.left
    self.mirror_tree(node.left)
    self.mirror_tree(node.right)

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def solve(self, tree):
    queue = Queue()
    queue.put(tree.root)

    while not queue.empty():
      node = queue.get()
      node.left, node.right = node.right, node.left

      if node.left: queue.put(node.left)
      if node.right: queue.put(node.right)

    return tree.level_order()

test_class(Solution2, examples)

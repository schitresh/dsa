from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_hash

# Given a binary tree, convert the binary tree to its mirror tree. Mirror of a binary
# tree is another binary tree with left and right children of all non-leaf nodes
# interchanged.

examples = [
  {
    'input': [
      binary_tree_from_level_hash([{ 1: [2, 2] }, { 3: [4, None] }]),
    ],
    'output': [[1], [3, 2], [4]]
  },
  {
    'input': [
      binary_tree_from_level_hash([{ 1: [2, 3] }, { 2: [4, 5] }]),
    ],
    'output': [[1], [3, 2], [5, 4]],
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

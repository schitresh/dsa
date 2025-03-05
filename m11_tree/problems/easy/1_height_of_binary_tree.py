from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_hash

# Given a binary tree, find the maximum depth of the tree. The maximum depth or height
# of a tree is the number of edges in the tree from the root to the deepest node.

examples = [
  {
    'input': [binary_tree_from_level_hash([
      { 12: [8, 18] },
      { 8: [5, 11] }
    ])],
    'output': 2,
  },
  {
    'input': [binary_tree_from_level_hash([
      { 1: [2, 3] },
      { 2: [4, None], 3: [None, 5] },
      { 5: [6, 7] }
    ])],
    'output': 3,
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(log(n)), where height = log(n)
class Solution:
  def solve(self, tree):
    return self.height_of_node(tree.root)

  def height_of_node(self, node):
    if not node: return -1

    height_left = self.height_of_node(node.left)
    height_right = self.height_of_node(node.right)

    return 1 + max(height_left, height_right)

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def solve(self, tree):
    height = -1
    queue = Queue()
    queue.put([tree.root, 0])

    while not queue.empty():
      node, level = queue.get()
      height = max(height, level)

      if node.left: queue.put([node.left, level + 1])
      if node.right: queue.put([node.right, level + 1])

    return height

test_class(Solution2, examples)

# Iterative BFS without tracking level
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution3:
  def solve(self, tree):
    height = -1
    queue = Queue()
    queue.put(tree.root)

    while not queue.empty():
      level_size = len(queue.queue)

      for _ in range(level_size):
        node = queue.get()

        if node.left: queue.put(node.left)
        if node.right: queue.put(node.right)

      height += 1

    return height

test_class(Solution3, examples)

from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given two binary trees, find if both of them are identical or not. Two trees are
# identical when they have the same data and the arrangement of data is also the same.

examples = [
  {
    'input': [
      binary_tree_from_level_array([[1], [[2, 3]], [[4, None], None]]),
      binary_tree_from_level_array([[1], [[2, 3]], [[4, None], None]]),
    ],
    'output': True,
  },
  {
    'input': [
      binary_tree_from_level_array([[1], [[2, 3]], [[4, None], None]]),
      binary_tree_from_level_array([[1], [[2, 3]], [None, [4, None]]]),
    ],
    'output': False,
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, tree1, tree2):
    return self.compare_tree(tree1.root, tree2.root)

  def compare_tree(self, node1, node2):
    if not node1 and not node2: return True
    if not node1 or not node2: return False
    if node1.key != node2.key: return False

    left_subtree = self.compare_tree(node1.left, node2.left)
    right_subtree = self.compare_tree(node1.right, node2.right)

    return left_subtree and right_subtree

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def solve(self, tree1, tree2):
    queue = Queue()
    queue.put([tree1.root, tree2.root])

    while not queue.empty():
      node1, node2 = queue.get()
      if not node1 and not node2: continue
      if not node1 or not node2: return False
      if node1.key != node2.key: return False

      queue.put([node1.left, node2.left])
      queue.put([node1.right, node2.right])

    return True

test_class(Solution2, examples)

# Todo: Morris Traversal
# Time Complexity: O(n)
# Space Complexity: O(1)

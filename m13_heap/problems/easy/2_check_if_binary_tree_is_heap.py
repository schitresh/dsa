from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, check if it has heap property or not.
# Binary tree needs to fulfil the following two conditions for being a heap:
# 1. It should be a complete tree, i.e. all levels except the last should be full.
# 2. Every node’s value should be greater than or equal to its child node (considering
# max-heap).

examples = [
  {
    'input': [binary_tree_from_level_array([
      [97], [[46, 37]], [[12, 3], [7, 31]]
    ])],
    'output': True,
  },
  {
    'input': [binary_tree_from_level_array([
      [97], [[46, 37]], [[12, 3], [7, 31]], [[6, 9], None, None, None]
    ])],
    'output': True,
  },
  {
    'input': [binary_tree_from_level_array([
      [97], [[46, 37]], [[12, 3], [7, 31]], [None, [2, 4], None, None]
    ])],
    'output': False,
  },
  {
    'input': [binary_tree_from_level_array([
      [97], [[46, 37]], [[12, 3], None], [[6, 9], None, None, None]
    ])],
    'output': False,
  },
]

# Using Recursive DFS and calculating Height
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution:
  def solve(self, tree):
    self.heap = True
    self.is_heap(tree.root)
    return self.heap

  def is_heap(self, node):
    if not node: return -1

    if node.left and node.left.key > node.key:
      self.heap = False
      return -1

    if node.right and node.right.key > node.key:
      self.heap = False
      return -1

    left_height = self.is_heap(node.left)
    right_height = self.is_heap(node.right)

    if abs(left_height - right_height) > 1:
      self.heap = False
      return -1

    return 1 + max(left_height, right_height)

test_class(Solution, examples)

# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution2:
  def solve(self, tree):
    queue = Queue()
    queue.put(tree.root)
    height_diff = 0

    while not queue.empty():
      level_size = len(queue.queue)
      missing_child = False

      for _ in range(level_size):
        node = queue.get()

        if node.left:
          if node.left.key > node.key: return False
          queue.put(node.left)

        if node.right:
          if node.right.key > node.key: return False
          queue.put(node.right)

        if not node.left or not node.right:
          missing_child = True

      if missing_child:
        if height_diff > 1: return False
        height_diff += 1

    return True

test_class(Solution2, examples)

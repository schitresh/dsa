from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, find the largest value in each level.

examples = [
  {
    'input': [binary_tree_from_level_array([[1], [[2, 3]]])],
    'output': [1, 3]
  },
  {
    'input': [binary_tree_from_level_array([[4], [[9, 2]], [[3, 5], [None, 7]]])],
    'output': [4, 9, 7]
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, tree):
    self.level_largest = []
    self.cal_level_largest(tree.root, 0)
    return self.level_largest

  def cal_level_largest(self, node, level):
    if not node: return

    if len(self.level_largest) - 1 < level:
      self.level_largest.append(node.key)
    else:
      self.level_largest[level] = max(self.level_largest[level], node.key)

    self.cal_level_largest(node.left, level + 1)
    self.cal_level_largest(node.right, level + 1)

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def solve(self, tree):
    level_largest = []
    queue = Queue()
    queue.put(tree.root)

    while not queue.empty():
      level_size = len(queue.queue)
      curr_max = float('-inf')

      for _ in range(level_size):
        node = queue.get()
        curr_max = max(curr_max, node.key)
        if node.left: queue.put(node.left)
        if node.right: queue.put(node.right)

      level_largest.append(curr_max)

    return level_largest

test_class(Solution2, examples)

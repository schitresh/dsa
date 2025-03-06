from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, check for every node whether its value is equal to the sum of
# values of its immediate left and right child. For NULL values, consider the value to
# be 0. Also, leaves are considered to follow the property.

examples = [
  {
    'input': [binary_tree_from_level_array([[10], [[8, 2]], [[3, 5], [2, None]]])],
    'output': True
  },
  {
    'input': [binary_tree_from_level_array([[10], [[8, 2]], [[2, 5], [2, None]]])],
    'output': False,
  },
  {
    'input': [binary_tree_from_level_array([[35], [[20, 15]], [[15, 5], [10, 5]]])],
    'output': True
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution:
  def solve(self, tree):
    return self.children_sum_property(tree.root)

  def children_sum_property(self, node):
    if not node: return True
    if not node.left and not node.right: return True

    left_val = 0
    right_val = 0
    if node.left: left_val = node.left.key
    if node.right: right_val = node.right.key

    if node.key != left_val + right_val: return False
    return (self.children_sum_property(node.left)
      and self.children_sum_property(node.right))

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
      if not node.left and not node.right: continue

      left_val = 0
      right_val = 0
      if node.left: left_val = node.left.key
      if node.right: right_val = node.right.key

      if node.key != left_val + right_val: return False
      if node.left: queue.put(node.left)
      if node.right: queue.put(node.right)

    return True

test_class(Solution2, examples)

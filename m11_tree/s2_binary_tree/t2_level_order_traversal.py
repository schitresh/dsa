from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import sample_binary_tree

examples = [
  {
    'input': [sample_binary_tree()],
    'output': [['a'], ['b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j'], ['k']]
  }
]

# Level order recursion using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tree):
    self.level_traversal = []

    level = 0
    while self.traverse_level_order(tree.root, 0, level):
      level = level + 1

    return self.level_traversal

  def traverse_level_order(self, node, node_level, level):
    if not node: return False

    if node_level == level:
      if level == len(self.level_traversal):
        self.level_traversal.append([])
      self.level_traversal[level].append(node.key)
      return True

    left = self.traverse_level_order(node.left, node_level + 1, level)
    right = self.traverse_level_order(node.right, node_level + 1, level)

    return left or right

test_class(Solution, examples)

# Level order recursion using DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree):
    self.level_traversal = []
    self.traverse_level_order(tree.root, 0)
    return self.level_traversal

  def traverse_level_order(self, node, level):
    if not node: return

    if level == len(self.level_traversal):
      self.level_traversal.append([])
    self.level_traversal[level].append(node.key)

    if node.left: self.traverse_level_order(node.left, level + 1)
    if node.right: self.traverse_level_order(node.right, level + 1)

test_class(Solution2, examples)

# Level order iterative using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, tree):
    traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([tree.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(traversal):
        traversal.append([])
      traversal[level].append(node.key)

      if node.left: queue.put([node.left, level + 1])
      if node.right: queue.put([node.right, level + 1])

    return traversal

test_class(Solution3, examples)

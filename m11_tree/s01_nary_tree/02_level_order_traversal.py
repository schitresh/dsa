from queue import Queue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Level Order Traversal
# Traverse all the nodes of a lower level before moving to any higher level node

examples = [
  {
    'input': [sample_nary_tree()],
    'output': [
      ['a'], ['b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm'], ['n']
    ],
  },
]

# Using Recursion based DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, tree):
    self.level_traversal = []
    self.traverse_level_order(tree.root, 0)
    return self.level_traversal

  def traverse_level_order(self, node, level):
    if not node: return

    if level == len(self.level_traversal):
      self.level_traversal.append([])

    self.level_traversal[level].append(node.key)

    for child in node.children:
      self.traverse_level_order(child, level + 1)

test_class(Solution, examples)

# Using Iteration based BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, tree):
    level_traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([tree.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(level_traversal):
        level_traversal.append([])
      level_traversal[level].append(node.key)

      for child in node.children:
        queue.put([child, level + 1])

    return level_traversal

test_class(Solution2, examples)

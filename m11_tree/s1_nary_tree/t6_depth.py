from queue import Queue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Given an n-ary tree containing positive node values, find the depth of the tree.
# Height is the number of edges on longest path from the node to a leaf node
# Depth is the number of edges on longest path from the root to the node
# Height of tree = Depth of tree
# Height of node + Depth of node = Height/Depth of tree

examples = [
  {
    'input': [sample_nary_tree(), 'n'],
    'output': 4
  },
  {
    'input': [sample_nary_tree(), 'l'],
    'output': 3
  }
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(h), due to recursive stack
class Solution:
  def solve(self, tree, key):
    node = tree.search_node(key)
    return self.depth_of_node(tree.root, node)

  def depth_of_node(self, root, node):
    if not root or not node: return
    if root == node: return 0

    for child in root.children:
      depth = self.depth_of_node(child, node)
      if depth is not None: return 1 + depth

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Auxiliary Space: O(h)
class Solution2:
  def solve(self, tree, key):
    node = tree.search_node(key)
    return self.depth_of_node(tree.root, node)

  def depth_of_node(self, root, node):
    if not root or not node: return

    depth = 0
    queue = Queue()
    queue.put([root, 0])

    while not queue.empty():
      front, level = queue.get()
      if front == node:
        depth = level
        break

      for child in front.children:
        queue.put([child, level + 1])

    return depth

test_class(Solution2, examples)

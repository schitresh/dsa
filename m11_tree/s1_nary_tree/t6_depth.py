from queue import Queue
from nary_tree import NaryTree
from nary_tree_utils import test_class

# Height is the number of edges on longest path from the node to a leaf node
# Depth is the number of edges on longest path from the root to the node
# Height of tree = Depth of tree
# Height of node + Depth of node = Height/Depth of tree

examples = [
  {
    'input': ['n'],
    'output': 4
  },
  {
    'input': ['l'],
    'output': 3
  }
]

# Recursive Approach
class Tree(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
  def depth(self, key):
    node = self.search_node(key)
    return self.depth_of_node(self.root, node)

  def depth_of_node(self, root, node):
    if not root or not node: return
    if root == node: return 0

    for child in root.children:
      depth = self.depth_of_node(child, node)
      if depth is not None: return 1 + depth

test_class(Tree, 'depth', examples)

# Using BFS
class Tree2(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def depth(self, key):
    node = self.search_node(key)
    return self.depth_of_node(self.root, node)

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

test_class(Tree2, 'depth', examples)

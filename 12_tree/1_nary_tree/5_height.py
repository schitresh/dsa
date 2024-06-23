from queue import Queue
from nary_tree import NaryTree
from nary_tree_utils import test_class

# Height is the number of edges on longest path from the node to a leaf node
# Depth is the number of edges on longest path from the root to the node
# Height of tree = Depth of tree
# Height of node + Depth of node = Height/Depth of tree

# Recursive Approach
class Tree(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
  def height(self, key):
    node = self.search_node(key)
    return self.height_of_node(node)

  def height_of_node(self, node):
    if not node: return

    height = 0
    for child in node.children:
      child_height = self.height_of_node(child)
      height = max(height, 1 + child_height)

    return height

# Using BFS
class Tree2(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def height(self, key):
    node = self.search_node(key)
    return self.height_of_node(node)

  def height_of_node(self, node):
    if not node: return

    height = 0
    queue = Queue()
    queue.put([node, 0])

    while not queue.empty():
      front, level = queue.get()
      height = max(height, level)

      for child in front.children:
        queue.put([child, level + 1])

    return height

examples = [
  {
    'input': ['a'],
    'output': 4
  },
  {
    'input': ['l'],
    'output': 1
  }
]

test_class(Tree, 'height', examples)
test_class(Tree2, 'height', examples)

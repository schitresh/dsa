from queue import Queue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Height is the number of edges on longest path from the node to a leaf node
# Depth is the number of edges on longest path from the root to the node
# Height of tree = Depth of tree
# Height of node + Depth of node = Height/Depth of tree

examples = [
  {
    'input': [sample_nary_tree(), 'a'],
    'output': 4
  },
  {
    'input': [sample_nary_tree(), 'l'],
    'output': 1
  }
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, tree, key):
    node = tree.search_node(key)
    return self.height_of_node(node)

  def height_of_node(self, node):
    if not node: return

    height = 0
    for child in node.children:
      child_height = self.height_of_node(child)
      height = max(height, 1 + child_height)

    return height

test_class(Solution, examples)

# Iterative BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree, key):
    node = tree.search_node(key)
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

test_class(Solution2, examples)

from queue import Queue
from nary_tree import NaryTree, Node
from nary_tree_utils import test_class

# Level Order Traversal
# Traverse all the nodes of a lower level before moving to any higher level node

# Using Recursion based DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Tree:
  def __init__(self, root = None):
    self.root = Node(root)
    self.level_traversal = []

  def level_order(self):
    self.level_traversal = []
    self.traverse_level_order(self.root, 0)
    return self.level_traversal

  def traverse_level_order(self, node, level):
    if not node: return

    if level == len(self.level_traversal):
      self.level_traversal.append([])
    self.level_traversal[level].append(node.key)

    for child in node.children:
      self.traverse_level_order(child, level + 1)

# Using Iteration based BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Tree2(NaryTree):
  def level_order(self):
    level_traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(level_traversal):
        level_traversal.append([])
      level_traversal[level].append(node.key)

      for child in node.children:
        queue.put([child, level + 1])

    return level_traversal

examples = [
  {
    'input': [],
    'output': [['a'], ['b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm'], ['n']]
  }
]

test_class(Tree, 'level_order', examples)
test_class(Tree2, 'level_order', examples)

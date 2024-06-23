from queue import LifoQueue
from nary_tree import NaryTree, Node
from nary_tree_utils import test_class

class Tree(NaryTree):
  def __init__(self, *args):
    super().__init__(*args)
    self.leaves = []

  def leaf_keys(self):
    self.reach_leaf_nodes(self.root)
    return self.leaves

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space which can be n in worst case
  def reach_leaf_nodes(self, node):
    if not node:
      return

    if len(node.children) == 0:
      self.leaves.append(node.key)

    for child in node.children:
      self.reach_leaf_nodes(child)

class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def leaf_keys(self):
    leaf_nodes = []
    # Stack used for DFS, Can use Queue instead for BFS
    stack = LifoQueue()
    stack.put(self.root)

    while not stack.empty():
      node = stack.get()

      if len(node.children) == 0:
        leaf_nodes.append(node.key)

      for child in reversed(node.children):
        stack.put(child)

    return leaf_nodes


examples = [
  {
    'input': [],
    'output': ['k', 'g', 'c', 'h', 'n', 'm', 'j', 'e']
  }
]

test_class(Tree, 'leaf_keys', examples)
test_class(Tree2, 'leaf_keys', examples)

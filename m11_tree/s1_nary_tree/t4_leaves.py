from queue import LifoQueue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Return values of all the leaf nodes of the given tree from left to right.

examples = [
  {
    'input': [sample_nary_tree()],
    'output': ['k', 'g', 'c', 'h', 'n', 'm', 'j', 'e']
  }
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
# Recursive stack will take O(h) space which can be n in worst case
class Solution:
  def solve(self, tree):
    self.leaves = []
    self.reach_leaf_nodes(tree.root)
    return self.leaves

  def reach_leaf_nodes(self, node):
    if not node: return

    if len(node.children) == 0:
      self.leaves.append(node.key)

    for child in node.children:
      self.reach_leaf_nodes(child)

test_class(Solution, examples)

# Iterative DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree):
    leaf_nodes = []
    # Stack used for DFS, Can use Queue instead for BFS
    stack = LifoQueue()
    stack.put(tree.root)

    while not stack.empty():
      node = stack.get()

      if len(node.children) == 0:
        leaf_nodes.append(node.key)

      for child in reversed(node.children):
        stack.put(child)

    return leaf_nodes

test_class(Solution2, examples)

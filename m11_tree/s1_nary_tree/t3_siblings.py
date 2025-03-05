from queue import Queue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Given an N-ary tree and an element X, find the siblings of the node with the value X.

examples = [
  {
    'input': [sample_nary_tree(), 'a'],
    'output': []
  },
  {
    'input': [sample_nary_tree(), 'd'],
    'output': ['b', 'c', 'e']
  },
  {
    'input': [sample_nary_tree(), 'i'],
    'output': ['h', 'j']
  }
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
# Recursive stack will take O(h) space which can be n in worst case
class Solution:
  def solve(self, tree, key):
    parent = self.parent(tree.root, key)
    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

  def parent(self, node, key):
    if not node:
      return

    for child in node.children:
      if child.key == key:
        return node

      parent = self.parent(child, key)
      if parent: return parent

test_class(Solution, examples)

# Iterative DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree, key):
    queue = Queue()
    queue.put(tree.root)
    parent = None

    while not queue.empty():
      node = queue.get()

      for child in node.children:
        if child.key == key:
          parent = node
          break

        queue.put(child)

      if parent: break

    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

test_class(Solution2, examples)

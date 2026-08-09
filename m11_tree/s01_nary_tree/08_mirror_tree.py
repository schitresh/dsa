from queue import Queue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Given a tree, convert the tree to its mirror image.

examples = [
  {
    'input': [sample_nary_tree()],
    'output': [
      ['a'], ['e', 'd', 'c', 'b'], ['j', 'i', 'h', 'g', 'f'], ['m', 'l', 'k'], ['n']
    ],
  },
]

# Using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tree):
    queue = Queue()
    queue.put(tree.root)

    while not queue.empty():
      node = queue.get()
      node.children.reverse()

      for child in node.children:
        queue.put(child)

    return tree.level_order()

test_class(Solution, examples)

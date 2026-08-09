from utils import test_class
from m11_tree.library.binary_search_tree import sample_bstree

examples = [
  {
    'input': [sample_bstree(), 5],
    'output': True
  },
  {
    'input': [sample_bstree(), 8],
    'output': True
  },
  {
    'input': [sample_bstree(), 7],
    'output': True
  },
  {
    'input': [sample_bstree(), 12],
    'output': False
  }
]

class Solution:
  def solve(self, tree, key):
    node = tree.root
    while node:
      if key < node.key:
        node = node.left
      elif key > node.key:
        node = node.right
      else:
        return True

    return False

test_class(Solution, examples)

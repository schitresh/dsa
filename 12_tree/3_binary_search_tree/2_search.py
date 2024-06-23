from binary_search_tree import BSTree
from binary_search_tree_utils import test_class

class Tree(BSTree):
  def search(self, key):
    node = self.root
    while node:
      if key < node.key:
        node = node.left
      elif key > node.key:
        node = node.right
      else:
        return True

    return False

examples = [
  {
    'input': [5],
    'output': True
  },
  {
    'input': [8],
    'output': True
  },
  {
    'input': [7],
    'output': True
  },
  {
    'input': [12],
    'output': False
  }
]

test_class(Tree, 'search', examples)

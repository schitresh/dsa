from nary_tree import NaryTree
from nary_tree_utils import test_class

class Tree(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space which can be n in worst case
  def search(self, key):
    return self.search_from_node(self.root, key)

  def search_from_node(self, node, key):
    if not node: return False

    if node.key == key: return True

    for child in node.children:
      result = self.search_from_node(child, key)
      if result: return True

    return False

examples = [
  {
    'input': ['n'],
    'output': True
  },
  {
    'input': ['zz'],
    'output': False
  }
]

test_class(Tree, 'search', examples)

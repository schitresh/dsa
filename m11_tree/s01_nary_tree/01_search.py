from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Given an n-ary tree, find if a given key exists or not

examples = [
  {
    'input': [sample_nary_tree(), 'n'],
    'output': True
  },
  {
    'input': [sample_nary_tree(), 'zz'],
    'output': False
  }
]

# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
# Recursive stack will take O(h) space which can be n in worst case
class Solution:
  def solve(self, tree, key):
    return self.search_from_node(tree.root, key)

  def search_from_node(self, node, key):
    if not node: return False

    if node.key == key: return True

    for child in node.children:
      result = self.search_from_node(child, key)
      if result: return True

    return False

test_class(Solution, examples)

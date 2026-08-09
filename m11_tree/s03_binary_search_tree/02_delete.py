from utils import test_class
from m11_tree.library.binary_search_tree import sample_bstree

examples = [
  {
    'input': [sample_bstree(), 10],
    'output': [[5], [2, 9], [1, 3, 8], [4, 6], [7]]
  },
  {
    'input': [sample_bstree(), 8],
    'output': [[5], [2, 9], [1, 3, 6, 10], [4, 7]]
  },
]

class Solution:
  def solve(self, tree, key):
    tree.root = self.delete_from_node(tree.root, key)
    return tree.level_order()

  def delete_from_node(self, node, key):
    if not node: return

    if key < node.key:
      node.left = self.delete_from_node(node.left, key)
    elif key > node.key:
      node.right = self.delete_from_node(node.right, key)
    else:
      if not node.left:
        temp = node.right
        del node
        return temp
      elif not node.right:
        temp = node.left
        del node
        return temp

      temp = node.right
      # Get min value
      while temp.left: temp = temp.left

      node.key = temp.key
      node.right = self.delete_from_node(node.right, node.key)

    return node

test_class(Solution, examples)

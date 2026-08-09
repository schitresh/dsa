from utils import test_class
from m11_tree.library.binary_search_tree import BSTree, Node, sample_bstree

examples = [
  {
    'input': [sample_bstree(), [11]],
    'output': [[5], [2, 9], [1, 3, 8, 10], [4, 6, 11], [7]]
  },
  {
    'input': [BSTree(), [5, 2, 1, 3, 4, 9, 8, 6, 7, 10]],
    'output': [[5], [2, 9], [1, 3, 8, 10], [4, 6], [7]]
  },
]

class Solution:
  def solve(self, tree, keys):
    for key in keys:
      tree.root = self.insert_from_node(tree.root, key)
    return tree.level_order()

  def insert_from_node(self, node, key):
    if not node: return Node(key)

    if node.key < key:
      node.right = self.insert_from_node(node.right, key)
    else:
      node.left = self.insert_from_node(node.left, key)

    return node

test_class(Solution, examples)

class Solution2:
  def solve(self, tree, keys):
    for key in keys:
      self.insert(tree, key)

    return tree.level_order()

  def insert(self, tree, key):
    prev = None
    temp = tree.root
    node = Node(key)

    while temp:
      prev = temp
      if temp.key < key:
        temp = temp.right
      else:
        temp = temp.left

    if not prev:
      tree.root = node
    elif prev.key < key:
      prev.right = node
    else:
      prev.left = node

test_class(Solution2, examples)

  # def delete(self, key):
  #   self.root = self.delete_from_node(self.root, key)

  # def delete_from_node(self, node, key):
  #   if not node: return

  #   if key < node.key:
  #     node.left = self.delete_from_node(node.left, key)
  #   elif key > node.key:
  #     node.right = self.delete_from_node(node.right, key)
  #   else:
  #     if not node.left:
  #       temp = node.right
  #       del node
  #       return temp
  #     elif not node.right:
  #       temp = node.left
  #       del node
  #       return temp

  #     temp = node.right
  #     # Get min value
  #     while temp.left: temp = temp.left

  #     node.key = temp.key
  #     node.right = self.delete_from_node(node.right, node.key)

  #   return node

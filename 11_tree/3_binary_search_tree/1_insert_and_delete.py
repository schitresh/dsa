from binary_search_tree import BSTree, Node

class Tree(BSTree):
  def insert(self, key):
    self.root = self.insert_from_node(self.root, key)

  def insert_from_node(self, node, key):
    if not node: return Node(key)

    if node.key < key:
      node.right = self.insert_from_node(node.right, key)
    else:
      node.left = self.insert_from_node(node.left, key)

    return node

  def insert_itr(self, key):
    prev = None
    temp = self.root
    node = Node(key)

    while temp:
      prev = temp
      if temp.key < key:
        temp = temp.right
      else:
        temp = temp.left

    if not prev:
      self.root = node
    elif prev.key < key:
      prev.right = node
    else:
      prev.left = node

  def delete(self, key):
    self.root = self.delete_from_node(self.root, key)

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

def test():
  tree = Tree()

  # [5]
  # [2, 9]
  # [[1, 3], [8, 10]]
  # [[[], [4]], [[6, ]]
  # [[[], []]], [[[, 7], []]]]
  keys = [5, 2, 1, 3, 4, 9, 8, 6, 7, 10]
  for key in keys:
    if key % 2 == 0: tree.insert(key)
    else: tree.insert(key)

  print(tree.level_order())
  tree.delete(8)
  print(tree.level_order())
  tree.delete(7)
  print(tree.level_order())
  tree.delete(5)
  print(tree.level_order())

test()

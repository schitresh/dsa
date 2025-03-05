from m11_tree.library.avl_tree import AvlTree

class Tree(AvlTree):
  # Time Complexity: O(log(n))
  # Auxliary Space: O(log(n)), for recursion stack
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
      node.right = self.delete_from_node(node.right, temp.key)

    return self.balance_deletion(node)

  # Time Complexity: O(1)
  # Auxliary Space: O(1)
  def balance_deletion(self, node):
    if not node: return

    left_height = self.height(node.left)
    right_height = self.height(node.right)

    node.height = 1 + max(left_height, right_height)
    balance = left_height - right_height

    if balance > 1:
      if self.balance_factor(node.left) >= 0:
        return self.rotate_right(node)
      else:
        return self.rotate_left_right(node)

    if balance < -1:
      if self.balance_factor(node.right) <= 0:
        return self.rotate_left(node)
      else:
        return self.rotate_right_left(node)

    return node

  def height(self, node):
    if not node: return 0
    return node.height

  def balance_factor(self, node):
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    return left_height - right_height

  def rotate_left(self, node):
    print('l')
    right = node.right
    node.right = right.left
    right.left = node

    node.height = 1 + max(self.height(node.left), self.height(node.right))
    right.height = 1 + max(self.height(right.left), self.height(right.right))

    return right

  def rotate_right(self, node):
    print('r')
    left = node.left
    node.left = left.right
    left.right = node

    node.height = 1 + max(self.height(node.left), self.height(node.right))
    left.height = 1 + max(self.height(left.left), self.height(left.right))

    return left

  def rotate_left_right(self, node):
    print('lr')
    node.left = self.rotate_left(node.left)
    return self.rotate_right(node)

  def rotate_right_left(self, node):
    print('rl')
    node.right = self.rotate_right(node.right)
    return self.rotate_left(node)

def test():
  tree = Tree()

  keys = [60, 50, 40, 70, 80, 20, 30, 100, 90]
  for key in keys: tree.insert(key)
  print(tree.level_order())

  keys = [100, 60, 20, 80, 70, 90]
  for key in keys:
    tree.delete(key)
    print(tree.level_order())

test()

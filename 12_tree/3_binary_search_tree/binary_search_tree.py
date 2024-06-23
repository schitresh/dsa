class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def _insert(self, root, key):
    if not root: return Node(key)

    if root.key < key:
      root.right = self._insert(root.right, key)
    else:
      root.left = self._insert(root.left, key)

    return root

  def _insert_itr(self, key):
    prev = None
    temp = self.root

    while temp:
      prev = temp
      if temp.key < key: temp = temp.right
      else: temp = temp.left

    node = Node(key)
    if not prev: self.root = node
    elif prev.key < key: prev.right = node
    else: prev.left = node

  def _delete(self, root, key):
    if not root: return

    if root.key < key:
      root.right = self._delete(root.right, key)
    elif root.key > key:
      root.left = self._delete(root.left, key)
    else:
      if not root.left:
        temp = root.right
        del root
        return temp
      elif not root.right:
        temp = root.left
        del root
        return temp

      temp = root.right
      while temp.left: temp = temp.left

      root.key = temp.key
      root.right = self._delete(root.right, root.key)

    return root

  def _inorder(self, root):
    if not root: return

    if root.left: self._inorder(root.left)
    print(root.key, end=" ")
    if root.right: self._inorder(root.right)

  def _preorder(self, root):
    if not root: return

    print(root.key, end=" ")
    if root.left: self._preorder(root.left)
    if root.right: self._preorder(root.right)

  def _postorder(self, root):
    if not root: return

    if root.left: self._postorder(root.left)
    if root.right: self._postorder(root.right)
    print(root.key, end=" ")

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def insert_itr(self, key):
    self._insert_itr(key)

  def delete(self, key):
    self.root = self._delete(self.root, key)

  def inorder(self):
    self._inorder(self.root)
    print()

  def preorder(self):
    self._preorder(self.root)
    print()

  def postorder(self):
    self._postorder(self.root)
    print()

bst = BST()
for i in range(6): bst.insert(i)
for i in range(10, 5, -1): bst.insert_itr(i)
for i in range(0, 10, 3): bst.delete(i)

bst.inorder()
bst.preorder()
bst.postorder()

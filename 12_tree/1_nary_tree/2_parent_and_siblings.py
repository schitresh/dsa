from queue import Queue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(Node, children))

class Tree:
  def __init__(self, root = None):
    self.root = Node(root)

  def siblings(self, key):
    parent = self.parent(self.root, key)
    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def parent(self, node, key):
    if not node:
      return

    for child in node.children:
      if child.key == key:
        return node

      parent = self.parent(child, key)
      if parent: return parent

class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def siblings(self, key):
    queue = Queue()
    queue.put(self.root)
    parent = None

    while not queue.empty():
      node = queue.get()

      for child in node.children:
        if child.key == key:
          parent = node
          break

        queue.put(child)

      if parent: break

    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

def test(klass):
  print_class_name(klass)
  tree = sample_tree1(klass)
  print(tree.siblings('a')) # []
  print(tree.siblings('d')) # [b, c, e]
  print(tree.siblings('i')) # [h, j]

test(Tree)
test(Tree2)

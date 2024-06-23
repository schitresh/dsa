from queue import Queue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(Node, children))

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree:
  def __init__(self, root = None):
    self.root = Node(root)
    self.tree_string = ''

  def serialize(self):
    self.tree_string = ''
    self.serializer(self.root)
    return self.tree_string

  def serializer(self, node):
    if not node:
      return

    self.tree_string += node.key + ' '

    for child in node.children:
      self.serializer(child)

    self.tree_string += ') '

  def deserialize(self):
    tree_keys = self.tree_string.split(' ')
    self.tree_string = ''
    iterator = iter(tree_keys)
    self.root = self.deserializer(iterator)

  def deserializer(self, iterator):
    key = next(iterator)
    if not key or key == ')':
      return

    node = Node(key)
    while True:
      child = self.deserializer(iterator)
      if not child: break
      node.children.append(child)

    return node

  def level_order(self):
    level_order_traversal = []
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(level_order_traversal):
        level_order_traversal.append([])
      level_order_traversal[level].append(node.key)

      for child in node.children:
        queue.put([child, level + 1])

    return level_order_traversal

def test(klass):
  print_class_name(klass)
  tree = sample_tree1(klass)
  print(tree.level_order())
  tree.serialize()
  print(tree.tree_string)
  tree.deserialize()
  print(tree.level_order())

test(Tree)

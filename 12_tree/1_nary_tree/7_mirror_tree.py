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

  def mirror(self):
    queue = Queue()
    queue.put(self.root)

    while not queue.empty():
      node = queue.get()
      node.children.reverse()

      for child in node.children:
        queue.put(child)

  def level_order(self):
    level_order_traversal = []
    # Use Stack for iteration based DFS
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
  tree.mirror()
  print(tree.level_order())

test(Tree)

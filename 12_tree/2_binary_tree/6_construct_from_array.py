from binary_tree import Node
from binary_tree_array import sample_tree_array
from queue import Queue
from utils import print_class_name

# Given the array representation of binary tree
# Construct the binary tree using nodes
class Tree:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def construct_from_array(self, array):
    queue = Queue()
    queue.put(0)

    self.root = Node(array[0])
    array[0] = self.root

    while not queue.empty():
      index = queue.get()
      node = array[index]

      left_index = 2 * index + 1
      right_index = 2 * index + 2

      if array[left_index]:
        node.left = Node(array[left_index])
        array[left_index] = node.left
        queue.put(left_index)

      if array[right_index]:
        node.right = Node(array[right_index])
        array[right_index] = node.right
        queue.put(right_index)

  def level_order(self):
    traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(traversal):
        traversal.append([])
      traversal[level].append(node.key)

      if node.left: queue.put([node.left, level + 1])
      if node.right: queue.put([node.right, level + 1])

    return traversal

def test(klass):
  print_class_name(klass)
  tree = klass()
  array = sample_tree_array()
  tree.construct_from_array(array)
  print(tree.level_order())

test(Tree)

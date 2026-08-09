from queue import Queue
from m11_tree.library.binary_tree import BinaryTree, Node
from m11_tree.library.binary_tree_array import sample_btree_array
from utils import test_class

# Given the array representation of binary tree
# Construct the binary tree using nodes

examples = [
  {
    'input': [sample_btree_array()],
    'output': [['a'], ['b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j'], ['k']]
  }
]

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    queue = Queue()
    queue.put(0)

    tree = BinaryTree(array[0])
    array[0] = tree.root

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

    return tree.level_order()

test_class(Solution, examples)

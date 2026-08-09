from m7_linked_list.library.doubly_list import doubly_list_from_array
from utils import test_class

# Given a doubly linked list, reverse it using recursion.

examples = [
  {
    'input': [doubly_list_from_array([10, 7, 16, 9, 20, 5])],
    'output': [
      [5, 20, 9, 16, 7, 10],
      [10, 7, 16, 9, 20, 5] # backwards
    ]
  },
  {
    'input': [doubly_list_from_array([0, -2, 2, -1, 3, 1])],
    'output': [
      [1, 3, -1, 2, -2, 0],
      [0, -2, 2, -1, 3, 1] # backwards
    ]
  },
]

# Insertion Sort
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, dlist):
    head = dlist.head
    tail = self.reverse_dlist(head)

    dlist.head = tail
    dlist.tail = head
    return [dlist.elements(), dlist.elements_backward()]

  def reverse_dlist(self, node):
    if not node: return

    node_next = node.next
    node.next = node.prev
    node.prev = node_next

    return self.reverse_dlist(node_next) or node

test_class(Solution, examples)

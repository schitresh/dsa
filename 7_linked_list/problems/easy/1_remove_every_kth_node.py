import sys
sys.path.append('../../library')
from linked_list import linked_list_from_array

from utils import test_class

# Given a singly linked list, remove every kth node of the linked list. Assume that
# k is always less than or equal to the length of the linked list.

examples = [
  {
    'input': [2, linked_list_from_array([1, 2, 3, 4, 5, 6])],
    'output': [1, 3, 5]
  },
  {
    'input': [3, linked_list_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
    'output': [1, 2, 4, 5, 7, 8, 10]
  }
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, k, llist):
    prev = None
    temp = llist.head
    steps = 0

    while temp:


      if steps % k == 0:
        if prev:
          prev.next = temp.next
          del temp
          temp = prev.next
        else:
          llist.head = temp.next
          del temp
          temp = llist.head
      else:
        prev = temp
        temp = temp.next

    return llist.elements()

test_class(Solution, examples)

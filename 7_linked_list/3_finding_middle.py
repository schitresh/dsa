from linked_list import linked_list_from_array
from utils import test_class

examples = [
  {
    'input': [linked_list_from_array([1, 2, 3, 4, 5, 6]).head],
    'output': 3
  },
  {
    'input': [linked_list_from_array([1, 2, 3, 4, 5, 6, 7]).head],
    'output': 4
  }
]

class Solution:
  def solve(self, head):
    if not head:
      return

    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    return slow.key

test_class(Solution, examples)

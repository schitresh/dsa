from circular_list import circular_list_from_array
from linked_list import linked_list_from_array
from utils import test_class

def linked_list_with_loop():
  linked_list = linked_list_from_array([1, 2, 3, 4, 5, 6])
  linked_list.last_node().next = linked_list.search(3)
  return linked_list

examples = [
  {
    'input': [linked_list_with_loop().head],
    'output': True
  },
  {
    'input': [circular_list_from_array([1, 2, 3, 4, 5, 6]).head],
    'output': True
  },
  {
    'input': [linked_list_from_array([1, 2, 3, 4, 5, 6]).head],
    'output': False
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, head):
    if not head:
      return

    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        return True

    return False

test_class(Solution, examples)

from library.linked_list import linked_list_from_array
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

# By counting nodes
# Time Complexity: O(n), but requires two iterations
# Auxiliary Space: O(1)
class Solution:
  def solve(self, head):
    count = 0
    temp = head

    while temp:
      count += 1
      temp = temp.next

    temp = head
    middle_len = count // 2
    if count % 2 == 0: middle_len -= 1
    while middle_len:
      temp = temp.next
      middle_len -= 1

    return temp.key

test_class(Solution, examples)

# Using Floyd’s Cycle Finding Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, head):
    if not head:
      return

    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    return slow.key

test_class(Solution2, examples)

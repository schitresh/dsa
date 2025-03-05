from library.circular_list import circular_list_from_array
from library.linked_list import linked_list_from_array
from utils import print_class_name

def linked_list_with_loop():
  linked_list = linked_list_from_array([1, 2, 3, 4, 5, 6])
  linked_list.last_node().next = linked_list.search(3)
  return linked_list

def examples():
  return [
    {
      'input': [linked_list_with_loop().head],
      'output': False
    },
    {
      'input': [circular_list_from_array([1, 2, 3, 4, 5, 6]).head],
      'output': False
    },
    {
      'input': [linked_list_from_array([1, 2, 3, 4, 5, 6]).head],
      'output': False
    },
  ]

# By finding loop length
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, head):
    return self.detect_and_remove_loop(head)

  def detect_and_remove_loop(self, head):
    if not head:
      return

    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        self.remove_loop(head, slow)
        return

  def remove_loop(self, head, loop_node):
    loop_len = self.loop_len(loop_node)
    temp1 = head
    temp2 = head

    # Move temp2 ahead by loop_len
    while loop_len > 0:
      temp2 = temp2.next
      loop_len -= 1

    # Move both pointers simultaneously, since temp2 is ahead by loop_len
    # both will reach at the node where loop starts
    while temp1 != temp2:
      temp1 = temp1.next
      temp2 = temp2.next

    # Find the last node
    while temp2.next != temp1:
      temp2 = temp2.next

    temp2.next = None

  def loop_len(self, loop_node):
    temp1 = loop_node
    temp2 = loop_node.next
    loop_len = 1

    while temp1 != temp2:
      loop_len += 1
      temp2 = temp2.next

    return loop_len

# Without finding loop length
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, head):
    return self.detect_and_remove_loop(head)

  def detect_and_remove_loop(self, head):
    if not head:
      return

    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        self.remove_loop(head, slow)
        return

  # Let's say length of the linked list l = x + y + z such that
  # Length before loop is x, where slow & fast pointers meet is y, and remaining is z
  # So, dist(slow) = x + y and dist(fast) = l + y = x + 2y + z
  # Also, fast pointer travelled twice the slow pointer
  # That means 2 * dist(slow) = 2 * dist(fast)
  # 2x + 2y = x + 2y + z => x = z
  def remove_loop(self, head, loop_node):
    temp1 = head
    temp2 = loop_node

    while temp1.next != temp2.next:
      temp1 = temp1.next
      temp2 = temp2.next

    temp2.next = None

def test(klass):
  def detect_loop(head):
    if not head: return
    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast: return True

    return False

  print_class_name(klass)
  for example in examples():
    klass().solve(*example['input'])
    loop = detect_loop(*example['input'])
    result = loop == example['output']
    print(f'{result}:', loop)

  print()

test(Solution)
test(Solution2)

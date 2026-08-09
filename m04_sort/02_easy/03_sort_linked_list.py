from utils import test_class
from m7_linked_list.library.linked_list import linked_list_from_array

# Given a singly linked list, sort it in non-decreasing order.

examples = [
  {
    'input': [linked_list_from_array([10, 30, 20, 5])],
    'output': [5, 10, 20, 30],
  },
  {
    'input': [linked_list_from_array([20, 4, 3])],
    'output': [3, 4, 20],
  },
]

# Bubble Sort
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, llist):
    size = llist.length()

    for _ in range(size):
      prev = None
      temp = llist.head

      while temp.next:
        temp_next = temp.next

        if temp.key > temp_next.key:
          if prev:
            prev.next = temp_next
          else:
            llist.head = temp_next

          temp.next = temp_next.next
          temp_next.next = temp
          prev = temp_next
        else:
          prev = temp
          temp = temp_next

    return llist.elements()

test_class(Solution, examples)

# Insertion Sort
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, llist):
    curr = llist.head

    while curr:
      prev = None
      temp = llist.head

      while temp != curr and temp.key < curr.key:
        prev = temp
        temp = temp.next

      if temp == curr:
        curr = curr.next
        continue

      insert_before = temp

      while temp.next != curr:
        temp = temp.next

      if prev:
        prev.next = curr
      else:
        llist.head = curr

      temp.next = curr.next
      curr.next = insert_before

      curr = curr.next

    return llist.elements()

test_class(Solution2, examples)

# Merge Sort
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, llist):
    llist.head = self.merge_sort(llist.head)
    return llist.elements()

  def merge_sort(self, head):
    if not head or not head.next:
      return head

    left = head
    mid = self.mid_node(head)
    right = mid.next
    mid.next = None

    left = self.merge_sort(left)
    right = self.merge_sort(right)
    return self.merge(left, right)

  def merge(self, left, right):
    if not left: return right
    if not right: return left

    if left.key < right.key:
      left.next = self.merge(left.next, right)
      return left

    right.next = self.merge(left, right.next)
    return right

  def mid_node(self, head):
    slow = head
    fast = head

    while fast and fast.next:
      fast = fast.next.next
      if fast: slow = slow.next

    return slow

test_class(Solution3, examples)

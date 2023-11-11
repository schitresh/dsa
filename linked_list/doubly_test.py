from doubly import DoublyLinkedList

def test():
  linked_list = DoublyLinkedList()

  for i in range(5):
    linked_list.append(i)
  for i in range(5, 10):
    linked_list.prepend(i)
  linked_list.print()
  linked_list.print_backward()

  # linked_list.prepend(7)
  # linked_list.append(7)
  # linked_list.delete(7)
  # linked_list.print()

  # print(linked_list.search(5).key)

test()

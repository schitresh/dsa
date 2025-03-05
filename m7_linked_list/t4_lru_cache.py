class Node:
  def __init__(self, key, val) -> None:
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LruCache:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.count = 0
    self.map = {}
    self.head = None
    self.tail = None

  def get(self, key):
    node = self.map.get(key)
    if node:
      self.move_to_front(node)
      return node.val

  def set(self, key, val):
    node = self.map.get(key)
    if node:
      node.val = val
      self.move_to_front(node)
    else:
      if self.count >= self.capacity:
        self.remove()

      self.insert(key, val)

  def move_to_front(self, node):
    if self.count <= 1:
      return

    prev = node.prev
    next = node.next

    if prev:
      prev.next = next
    if next:
      next.prev = prev

    if self.tail == node:
      self.backtrack_tail()

    self.reassign_head(node)

  def reassign_head(self, node):
    node.prev = None
    node.next = self.head

    if self.head:
      self.head.prev = node

    self.head = node

  def backtrack_tail(self):
    if self.count <= 1:
      return

    temp = self.tail
    self.tail = temp.prev
    self.tail.next = None

    temp.prev = None
    return temp

  def insert(self, key, val):
    node = Node(key, val)
    self.map[key] = node

    self.reassign_head(node)

    if not self.tail:
      self.tail = node

    self.count += 1

  def remove(self):
    temp = self.tail.prev
    temp.next = None

    self.map[self.tail.key] = None
    del self.tail

    self.tail = temp
    self.count -= 1

  def print(self):
    temp = self.head
    while temp:
      if temp.next:
        print(temp.val, end=', ')
      else:
        print(temp.val)

      temp = temp.next

  def clean(self):
    temp = self.head

    while temp:
      self.head = temp.next

      self.map[temp.key] = None
      del temp

      temp = self.head
      self.count -= 1

    self.tail = None

def test():
  cache = LruCache(3)
  print('> Get 1')
  print(cache.get(1))

  print('> Add 1, 2, 3')
  cache.set(1, 'a')
  cache.set(2, 'b')
  cache.set(3, 'c')
  print('> Cache')
  cache.print()

  print('> Add 4')
  cache.set(4, 'd')
  print('> Cache')
  cache.print()

  print('> Get 1')
  print(cache.get(1))

  print('> Get 3')
  print(cache.get(3))
  print('> Cache')
  cache.print()

  print('> Update b to e')
  cache.set(2, 'e')
  print('> Cache')
  cache.print()

  print('> Clean')
  cache.clean()
  cache.print()

test()

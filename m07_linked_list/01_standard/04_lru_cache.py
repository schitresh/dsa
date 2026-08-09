# LRU (Least Recently Used) Cache
# Cache replacement algorithms are efficiently designed to replace the cache when the
# space is full. When the cache memory is full, LRU picks the data least recently used
# and removes it to make space for the new data. If some data is fetched or updated
# recently, then the priority of that data would be changed and assigned to the highest
# priority.

# Operations
# LruCache(c): Initialize LRU cache with positive size capacity c
# get(key): Returns the value of key if present
# And update the priority of key in the LRU cache
# put(key, value): Add or update the value of the key
# If the number of keys exceed the capacity, then dismiss the least recently used key

# Implementation using Array, Hashing, Heap
# If an array is used to store nodes (key-value pairs), the time complexity for the
# get & put operations will be O(n) since the key will need to be searched.
# With hashing, we can insert, get and delete in O(1) time, but changing priorities
# would take linear time. We can think of using heap along with hashing for priorities.
# We can find and remove the least recently used in O(log(n)) which is more than O(1)
# and changing priority in the heap would also be required.

# Implementation using Doubly Linked List and Hashing
# Manage element access and removal efficiently through a combination of a doubly linked
# list and a hash map.
# The priority of nodes in the doubly linked list is based on their distance from the
# head. Keys closer to the head are more recently used and those closer to the tail are
# less recently used.
# When adding a new key, insert it as a new node at the head. If the key is already
# present, get the corresponding node using hashmap, update its value and move it to the
# head. When the cache reaches its maximum capacity and a new key needs to be added,
# remove the node at the tail of the doubly linked list and from the hashmap.
# Time Complexity: O(1) for both get & put operations
# Auxiliary Space: O(n), for hashmap

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
    if not node: return None

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
    if self.count <= 1: return

    prev = node.prev
    next = node.next

    if prev: prev.next = next
    if next: next.prev = prev

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
    if self.count <= 1: return

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

  print('> Add 1(a), 2(b), 3(c)')
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

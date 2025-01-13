class Queue:
  def __init__(self):
    self.queue = []
    self._front = 0

  def size(self):
    return len(self.queue)

  def empty(self):
    return self.size() == 0

  def front(self):
    if self.empty(): return
    return self.queue[0]

  def push(self, item):
    self.queue.append(item)

  def pop(self):
    if self.empty(): return
    return self.queue.pop(0)

def test():
  queue = Queue()

  for i in range(1, 6):
    queue.push(i)

  print('Pop (1):', queue.pop())
  print('Size (4):', queue.size())
  print('Top (2):', queue.front())
  print('Empty (False):', queue.empty())

test()

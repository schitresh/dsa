class Queue:
  def __init__(self):
    self.queue = []

  def push(self, item):
    self.queue.append(item)

  def pop(self):
    return self.queue.pop(0) if not self.empty() else -1

  def size(self):
    return len(self.queue)

  def front(self):
    return -1 if self.empty() else self.queue[0]

  def empty(self):
    return self.size() == 0

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print('pop', q.pop())
print('size', q.size())
print('front', q.front())
print('empty', q.empty())

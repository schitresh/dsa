## Queue
- Operations
  - Push: O(1)
  - Pop: O(1)
  - Size: O(1)
  - IsEmpty: O(1)
- Types
  - Simple
  - Double Ended
  - Circular
  - Priority

## Application
- Job scheduling like printer spooling
- Inter-process communication using queues
- Producer & consumer queues
- Algorithms like breadth first search, topological sort, etc.

## Python
```py
from queue import Queue
queue = Queue()
queue = Queue(maxsize=10)
queue.put('a')
queue.get()
queue.qsize()
queue.empty()
queue.full()

# Dequeue (Double ended queue)
from collections import deque
queue = deque()
queue = deque(maxlen=10)
queue.append_left('a')
queue.pop()
queue.append('a')
queue.pop_left()
queue.clear()
queue.count(x)
queue.insert(i, x)
queue.remove(x)
queue.queue # To get the queue array
```

## Ruby
```rb
queue = Queue.new
queue << 2
queue.push(3)
queue.pop
queue.size
queue.empty?
```

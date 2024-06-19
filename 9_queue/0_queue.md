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
-

## Python
```py
from queue import Queue
stack = Queue()
stack = Queue(maxsize=10)
stack.put('a')
stack.get()
stack.qsize()
stack.empty()
stack.full()

from collections import deque
stack = deque()
stack = deque(maxlen=10)
stack.append_left('a')
stack.pop()
stack.append('a')
stack.pop_left()
stack.clear()
stack.count(x)
stack.insert(i, x)
stack.remove(x)
```

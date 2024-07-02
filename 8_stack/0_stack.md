## Stack
- Operations
  - Push: O(1)
  - Pop: O(1)
  - Size: O(1)
  - IsEmpty: O(1)
- Types
  - Fixed Size
  - Dyanmic Size

## Application
- Infix (a + b) to postfix (ab+)
- Forward backward navigation
- Undo redo
- Backtracking to store previous state
- OS: Memory management
- Compiler Design: Parsing & syntax analysis

## Python
```py
from queue import LifoQueue
stack = LifoQueue()
stack = LifoQueue(maxsize=10)
stack.put('a')
stack.get()
stack.qsize()
stack.empty()
stack.full()

from collections import deque
stack = deque()
stack = deque(maxlen=10)
stack.append('a')
stack.pop()
stack.clear()
stack.count(x)
stack.insert(i, x)
stack.remove(x)
stack.queue # To get the queue array
```

## Ruby
```rb
stack = []
stack << 2
stack << 3
stack.pop
stack.size
stack.empty?
```

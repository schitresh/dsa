## Heap
- Complete binary tree that satisfies the heap property
  - That is, for every node, the value of its children is less than or equal to its own value
  - Or, more than or equal to
- Heapify is the process to rearrange the elements to maintain the heap property
  - Nodes can be imbalanced due to some operation on that node
- Types
  - Max Heap: Values decrease as you move down the tree
  - Min heap: Values increase as you move down the tree
- Not suitable for searching, O(n) in worst case
- Operations
  - Insertion: O(log(n))
  - Deletion: O(log(n))
  - Heapify: O(log(n))
  - Min/Max element: O(1)
  - Searching: O(n) in worst case

## Applications
- Usually used to implement priority queues
  - Where the smallest (or the largest) element is always at the root
- Used in graph algorithms like prim's mst and dijkstra's shortest path

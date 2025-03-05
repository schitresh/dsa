## Properties
- Number of edges = Number of nodes - 1
- Maximum nodes at level L is 2^L
- Maximum nodes for height H is 2^H - 1
- Minimum height for N nodes is log2(N + 1)
- Minimum levels for L leaves is log2(L) + 1

## Types
### On basis of number of children
- Full binary tree
  - All nodes except leaf nodes have two children
- Degenerate binary tree
  - Each internal node has one chilid
  - Performance-wise same as linked list
- Skewed binary tree
  - Degenerate tree in which there are only left childs or right childs
  - Thus, there are two types: left-skewed binary tree, right-skewed binary tree

### On basis of completion of levels
- Complete binary tree
  - All the levels are completely filled except possibly the last level
  - Last level has all keys as left as possible
- Perfect binary tree
  - All internal nodes have two children and all leaf nodes are at the same level
  - Number of leaves = Number of internal nodes + 1
- Balanced binary tree
  - A binary tree is balanced if the height of the tree is O(log(Nodes))
  - Examples: AVL tree, Red-black tree
  - Good performance with O(log(n)) for search, insert, delete

### On basis of node values
- Binary search tree
  - Left subtree has nodes with keys lesser than node's key
  - Right subtree has nodes with keys greater than node's key
  - Left and right subtree must also be binary search trees
- AVL tree
  - Self-balancing binary search tree
  - Difference between heights of left and right subtrees is at most one
- Red black tree
  - Self-balancing binary search tree
  - Each node has an extra bit for color (red or black)
  - The color is used to ensure that
    - The tree remains balanced during insertions & deletions
  - Although the balance of the tree is not perfect
    - It is good enough to reduce the searching time around O(log(n))
- B tree
  - Self-balancing tree commonly used in databases and file systems
  - Characterized by a fixed maximum degree (or order)
    - Which determines the maximum children for any node
  - Each node can have multiple children
    - And multiple keys used to index and locate data items
- B+ tree
  - Variation of B tree optimized to store all data items in leaf nodes
  - Internal nodes contain only keys for indexing and locating data items
  - Allows faster searches and sequential access of data items
    - As leaf nodes are linked together in a linked list
- Segment tree
  - Stores information about intervals or segments
  - Static structure, i.e. it cannot be modified once built
  - Supports searching all the intervals that contain a query point
    - In O(log(n) + k) where k is the number of retrieved intervals

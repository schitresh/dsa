## AVL Tree
- Self-balancing binary search tree
  - where difference between heights of left and right subtrees for any node
  - cannot be more than one
- Balance Factor
  - The difference between the heights of the left and right subtrees for any node
- Most of the operations in BST like insert, delete, search, max, min, etc. take O(h)
  - If we make sure that height of the tree is log(n), i.e. almost balanced tree
  - Then these operations can be done in O(log(n))
- Faster lookups than normal binary search trees and red-black trees
- Insertion and removal operations are complicated as rotations are performed

## Rotations
- An AVL tree may rotate in one of the four ways to keep it balanced
- Let's say L() denotes left child and R() denotes right child
- Left Rotation
  - When a node is added to the right subtree of the right subtree
  - Do a single left rotation if the tree gets out of balance
  - A -> R(B) -> R(C) rotates to B -> L(A) + R(C)
- Right Rotation
  - When a node is added to the left subtree of the left subtree
  - Do a single right rotation if the tree gets out of balance
  - A -> L(B) -> L(C) rotates to B -> L(C) + R(A)
- Left-Right Rotation
  - When a node is added to the right subtree of the left subtree
  - First rotate left and then rotate right if the tree gets out of balance
  - Left: C -> L(A) -> R(B) rotates to C -> L(B) -> L(A)
  - Right: C -> L(B) -> L(A) rotates to B -> L(A) + R(C)
- Right-Left Rotation
  - When a node is added to the left subtree of the right subtree
  - First rotate right and then rotate left if the tree gets out of balance
  - Right: A -> R(C) -> L(B) rotates to A -> R(B) -> R(C)
  - Left: A -> R(B) -> R(C) rotates to B -> L(A) + R(C)

## Applications
- Used to index huge records in a database and to efficiently search in that
- For in-memory collections like sets, dictionaries, maps

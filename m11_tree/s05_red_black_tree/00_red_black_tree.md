## AVL Tree
- Self-balancing binary search tree with an attribute for color to maintain balance
  - Longest path from the root to any leaf is no more than twice the shortest path
- Most of the operations in BST like insert, delete, search, max, min, etc. take O(h)
  - If we make sure that height of the tree is log(n), i.e. almost balanced tree
  - Then these operations can be done in O(log(n))
- Faster lookups than normal binary search trees
- AVl trees are more balanced than red-black trees
  - But may cause more rotations during insertion and deletion
  - So red-black tree should be preferred
    - If the application involves frequent insertions & deletions

## Properties
- Each node is either red or black
- Root is always black
- Red nodes cannot have red children
- Each path from a node to its decendant leaves has the same number of black nodes
  - Also called the black height
- All leaves are black and NIL (no key)

## Balancing
- Recoloring and rotation are used for balancing
  - If recoloring doesn't work, then we go for rotation
- Insert a node similar to binary search tree and assign red color to it
  - If the node is root node, change its color to black
  - Else check the color of the parent node
    - If the parent has black color, let the current node be red
    - Else check the color of the node's uncle
      - If the uncle has red color, then
        - Change the parent and the uncle to color black
        - Change the grandfather to color red unless its the root
        - And repeat the process
      - Else do the rotation similar to AVL Tree
        - For Left & Right rotation
          - Swap colors of the grandparent and the parent
        - For Left Right & Right Left rotation
          - Swap colors of the grandparent and the inserted node

## Applications
- To implement ordered data structures lke sets, maps
- To implement graph algorithms like prim's mst and dijkstra's shortest path
- Used in memory allocation algorithms to manage memory blocks efficiently
- Used in K-mean clustering algorithm in machine learning to reduce time complexity

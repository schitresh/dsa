## Tree
- Collection of elements as nodes that are connected via edges
  - Such that there exists exactly one path between any two nodes
- Types
  - Binary tree
  - Ternary tree
  - N-ary or generic tree

```py
class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
```

## Terminologies
- Root Node
- Parent Node
- Child Node
- Internal Node
- Leaf Node
- Ancestor: Any predecessor node on the path from root to that node
- Descendent: Inverse of ancestor
- Sibling
- Neighbor: Parent or child nodes
- Subtree: Any node of the tree along with its descendant

## Properties
- Number of Edges: N - 1
- Level: Number of nodes on the path from root to that node
- Depth of Node: Length of the path from root to that node
  - Level = 1 + Depth
- Height of Tree: Longest path from root to a leaf node
- Height of Node: Longest path from node to a leaf node
  - Height of Node + Depth of Node = Height of Tree
- Degree of Tree: Maximum degree among all nodes
- Degree of Node: Count of subtrees attached to that node

## Application
- File system
- Data compresson like huffman coding
- Compiler design: syntax tree
- Database indexing: b tree, b+ tree
- Dictionaries with prefix loop using trie

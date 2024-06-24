## Graph
- Collection of nodes (or vertices) connected by edges

## Types
- Null: Graph with no edges
- Trivial: Graph with single vertex
- Undirected: Edges have no direction
- Directed: Edges have direction
- Connected: Any node can be visited from any node
- Disconnected: At least one node is not reachable from a node
- Regular: Degree of every vertex is K
- Complete: Each node has an edge to every other node
- Cycle: Graph is a cycle itself
- Cyclic: Graph contains at least one cycle
- Directed Acyclic: Directed graph with no cycle
- Bipartite
  - Graph in which bertices can be divided into two sets
  - Such that vertices in one set do not have any edge between them
- Weighted: Graph in which edges have weight (or value) associated with them
  - Undirected weighted graph
  - Directed weighted graph

## Representation
### Adjanceny Matrix
- Graph is stored in the form of 2D matrix
- Rows and columns denote vertices
- Each entry in the matrix represents the weight of the edge
- For unweighted graph, 1 can be used as the weight denoting that edge exists
- Operations
  - Adding Edge: O(1)
  - Remove Edge: O(1)
  - Initializing: O(N^2)

### Adjancency List
- Graph is stored as list of lists
- Where index denotes the node
- And list[node_1] denotes the other nodes connected to node_1
- Operations
  - Adding Edge: O(1)
  - Remove Edge: O(N)
  - Initializing: O(N)

## Applications
- To represent relationships between different entities
- To manipulate and analyze graphs
- Finding shortest path
- Detecting cycles
- Recommendation system
- Neural Networks

## Python
- Not inbuilt

## Ruby
- Not inbuilt

## Topological Sorting (or Order)
- Linear ordering of vertices
  - Such that for every directed edge u -> v, vertex u comes before v in the ordering
  - That is, all the dependent nodes appear after the source nodes
- There can be multiple topological orders
- Possible for only Directed Acyclic Graph (DAG)
  - For undirected graph
    - Both u -> v and v -> u are valid, so there is a contradiction
  - For cyclic graph
    - All vertices are indirectly dependent on each other creating contradiction

## Example
- Let's say we have these edges
  - 5 -> 0, 4 -> 0, 3 -> 1, 4 -> 1, 5 -> 2, 2 -> 3
- One topological order is 5, 4, 2, 3, 1, 0
  - For 5 -> 0, 4 -> 0: 5 & 4 appear before 0
  - For 3 -> 1, 4 -> 1: 3 & 4 apeear before 1
  - And so on
- Some other orders are
  - 4, 5, 2, 3, 1, 0
  - 4, 5, 0, 2, 3, 1
  - And so on

## Topological Order vs DFS
- Consider these edges: 0 -> 1, 1 -> 2, 3 -> 1, 3 -> 2
- DFS order: 0, 1, 2, 3
- Topological order: 3, 0, 1, 2
  - 3 should appear first because of 3 -> 1, 3 -> 2

## Applications
- Scheduling tasks or events based on dependencies
- Detect cycle in directed graphs
- Dependency resolution
- Deadlock detection

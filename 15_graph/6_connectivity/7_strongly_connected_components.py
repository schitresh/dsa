from utils import test_class

# Strongly Connected Components
# SCC of a directed graph is a maximal subgraph where every pair of vertices
# is mutually reachable
# That is, subset of vertices where every vertex is reachable from every other vertex
# in the same subset by traversing the directed edges

# Connectivity is applicable to undirected graphs
# SCC is applicable to directed graphs
# Conventional DFS cannot be used to SCC
# because there may not be directed path between different set of vertices
# Two different components can be connected by adding a edge between the two
# But the same is not true for SCCs due to its directional nature

examples = [
  {
    'input': [[[1, 3], [2], [3, 4], [], []]],
    'output': [[0], [1], [2], [3], [4]]
  },
  {
    'input': [[[1, 3], [2], [0], [4], [0]]],
    'output': [[0, 1, 2, 3, 4]]
  },
  {
    'input': [[[2, 3], [0], [1], [4], []]],
    'output': [[0, 1, 2], [3], [4]]
  },
]

# Time Complexity: O(V * (V + E))
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph):
    self.graph = graph

    all_scc = []
    is_scc_vertex = [False] * len(graph)

    # Traverse all the vertices and determine SCC
    for node in range(len(graph)):
      # If the vertex is already part of some SCC, then skip
      if is_scc_vertex[node]: continue

      # Insert the node into a new SCC and check if other vertices can be part of it
      scc = [node]
      for curr in range(node + 1, len(graph)):
        if is_scc_vertex[curr]: continue

        # If there is a path from node to curr and from curr to node
        # Then curr is part of the SCC started with node
        if self.is_path(node, curr) and self.is_path(curr, node):
          is_scc_vertex[curr] = True
          scc.append(curr)

      all_scc.append(scc)

    return all_scc

  def is_path(self, src, dest):
    visited = [False] * len(self.graph)
    return self.dfs(visited, src, dest)

  def dfs(self, visited, curr, dest):
    if curr == dest: return True

    visited[curr] = True
    for neighbor in self.graph[curr]:
      if visited[neighbor]: continue
      if self.dfs(visited, neighbor, dest):
        return True

    return False

test_class(Solution, examples)

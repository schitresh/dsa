from utils import test_class

# A directed graph has an eulerian cycle if these conditions are true
# (1) All vertices with non-zero degree belong to a single strongly connected component
# (2) For every vertex, in-degree is equal to out-degree

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': 'Eulerian Path'
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]],
    'output': 'None'
  },
  {
    'input': [[[1, 2, 3, 4], [0, 2], [0, 1], [0, 4], [0, 3]]],
    'output': 'Eulerian Cycle'
  },
]

# All middle vertices in eulerian path must have even degree
# Since we need at least two edges to pass through a vertex
# For eulerian cycle, any vertex can be middle vertex
# So all vertices must have an even degree
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    if not self.is_connected(graph):
      return 'None'

    odd_vertices = 0
    for neighbors in graph:
      if len(neighbors) % 2 == 1:
        odd_vertices += 1

    if odd_vertices == 0:
      return 'Eulerian Cycle'

    # Since an edge requires 2 vertices, there cannot be one odd vertex in a graph
    if odd_vertices == 2:
      return 'Eulerian Path'

    return 'None'

  def is_connected(self, graph):
    visited = [False] * len(graph)
    self.dfs(graph, visited, 0)

    if all(visited): return True
    return False

  def dfs(self, graph, visited, node):
    visited[node] = True

    for neighbor in graph[node]:
      if visited[neighbor]: continue
      self.dfs(graph, visited, neighbor)

test_class(Solution, examples)

from utils import test_class

# A directed graph has an eulerian cycle if these conditions are true
# (1) All vertices with non-zero degree belong to a single strongly connected component
# (2) For every vertex, in-degree is equal to out-degree

examples = [
  {
    'input': [[[1, 3], [2], [3, 4], [], []]],
    'output': False
  },
  {
    'input': [[[1, 3], [2], [0], [4], [0]]],
    'output': True
  },
  {
    'input': [[[2, 3], [0], [1], [4], []]],
    'output': True
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    if not self.is_scc_kosaraju(graph):
      return False

    in_degree = [0] * len(graph)
    for node in range(len(graph)):
      for neighbor in graph[node]:
        in_degree[neighbor] += 1

    for node in range(len(graph)):
      out_degree = len(graph[node])
      if out_degree != in_degree[node]:
        return False

    return True

  def is_scc_kosaraju(self, graph):
    visited = [False] * len(graph)

    self.dfs(graph, visited, 0)

    if not all(visited): return False

    visited = [False] * len(graph)
    transpose = self.get_transpose(graph)
    self.dfs(transpose, visited, 0)

    if not all(visited): return False

    return True

  def dfs(self, graph, visited, node):
    visited[node] = True

    for neighbor in graph[node]:
      if visited[neighbor]: continue
      self.dfs(graph, visited, neighbor)

  def get_transpose(self, graph):
    transpose = [[] for _ in range(len(graph))]

    for node in range(len(graph)):
      for neighbor in graph[node]:
        transpose[neighbor].append(node)

    return transpose


test_class(Solution, examples)

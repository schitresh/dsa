from queue import LifoQueue
from utils import test_class

# Given a directed graph, determine if a vertex j is reachable from another vertex i
# for all vertex pairs (i, j) in the given graph. Here, reachable means that there is a
# path from vertex i to j. The reachability matrix is called the transitive closure of a
# graph.

examples = [
  {
    'input': [[
      [1, 1, 0, 1],
      [0, 1, 1, 0],
      [0, 0, 1, 1],
      [0, 0, 0, 1],
    ]],
    'output': [
      [1, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 0, 1, 1],
      [0, 0, 0, 1],
    ],
  },
  {
    'input': [[
      [0, 1, 1, 0],
      [0, 0, 1, 0],
      [1, 0, 0, 1],
      [0, 0, 0, 0],
    ]],
    'output': [
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [0, 0, 0, 1],
    ],
  },
]

# Floyd Warshall Algorithm
# Time Complexity: O(V^3)
# Auxiliary Space: O(V^2)
class Solution:
  def solve(self, graph):
    # Initialize transitive closure to graph
    tclosure = [row[:] for row in graph]

    for k in range(len(graph)):
      for i in range(len(graph)):
        for j in range(len(graph)):
          if i == j:
            tclosure[i][j] = 1
            continue

          tclosure[i][j] = tclosure[i][j] or (tclosure[i][k] and tclosure[k][j])

    return tclosure

test_class(Solution, examples)

# Iterative DFS
# Time Complexity: O(V^3)
# Auxiliary Space: O(V^2)
class Solution2:
  def solve(self, graph):
    tclosure = [[0] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
      visited = [False] * len(graph)
      stack = LifoQueue()
      stack.put(i)

      while not stack.empty():
        vertex = stack.get()
        visited[vertex] = True
        tclosure[i][vertex] = 1

        for neighbor in range(len(graph)):
          if graph[vertex][neighbor] == 0: continue
          if visited[neighbor]: continue
          stack.put(neighbor)

    return tclosure

test_class(Solution2, examples)

# Recursive DFS
# Time Complexity: O(V^3)
# Auxiliary Space: O(V^2)
class Solution3:
  def solve(self, graph):
    self.graph = graph
    self.tclosure = [[0] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
      self.visited = [False] * len(graph)
      self.dfs(i, i)

    return self.tclosure

  def dfs(self, source, vertex):
    self.visited[vertex] = True
    self.tclosure[source][vertex] = 1

    for neighbor in range(len(self.graph)):
      if self.graph[vertex][neighbor] == 0: continue
      if self.visited[neighbor]: continue

      self.dfs(source, neighbor)

test_class(Solution3, examples)

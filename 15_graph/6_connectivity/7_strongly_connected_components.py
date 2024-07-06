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


# Tarjan's Algorithm
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Tarjan:
  def __init__(self) -> None:
    self.graph = [[]]
    self.all_scc = []
    self.disc = []
    self.low = []
    self.time = 0
    self.stack = []
    self.stack_member = []

  def solve(self, graph):
    self.graph = graph

    # Stores all the connected ancestors
    self.stack = []
    # Index array for faster check of whether a node is in the stack
    self.stack_member = [False] * len(graph)

    # Stores discovery times of vertices (When a vertex was visited)
    # So, it also tracks if a vertex was visited or not
    self.disc = [float('inf')] * len(graph)
    # Stores the earliest visited vertex that can be reached from the subtree rooted at u
    # low[u] = min(disc[u], disc[w]), where w is an ancestor of u
    # And there is a back edge from some descendant of u to w
    # E.g. in 1 -> 2, 2-> 3, 3 -> 1: 3 -> 1 is a back edge
    self.low = [float('inf')] * len(graph)

    for node in range(len(graph)):
      if self.disc[node] != float('inf'): continue
      self.dfs(node)

    return self.all_scc

  def dfs(self, node):
    self.stack.append(node)
    self.stack_member[node] = True

    self.disc[node] = self.time
    self.low[node] = self.time
    self.time += 1

    for neighbor in self.graph[node]:
      if self.disc[neighbor] == float('inf'):
        self.dfs(neighbor)

        # Check if subtree rooted at neighbor
        # has a connection to one of the ancestor of the node
        self.low[node] = min(self.low[node], self.low[neighbor])

      # Update low value of node only if neighbor is still in stack
      # That is, it's a back edge and not a cross edge
      elif self.stack_member[neighbor]:
        self.low[node] = min(self.low[node], self.disc[neighbor])

    # Head node is found
    if self.low[node] == self.disc[node]:
      temp = -1
      scc = []

      while temp != node:
        temp = self.stack.pop()
        self.stack_member[temp] = False
        scc.append(temp)

      self.all_scc.append(scc)

test_class(Solution, examples)
test_class(Tarjan, examples)

from utils import test_class

# Fleury's Algorithm
# Used for printing the Eulerian trail/path or cycle
# Make sure the graph has either 0 or 2 odd vertices
# If there are 0 odd vertices, start anywhere
# If there are 2 odd vertices, start at one of them
# Follow edges one at a time
# If there is a choice between a bridge and a non-bridge, choose the non-bridge
# Don't burn bridges so that we can come back

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [(2, 1), (1, 0), (0, 3), (3, 2), (2, 4)]
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7],
                [3, 4, 6]]],
    'output': []
  },
  {
    'input': [[[1, 2, 3, 4], [0, 2], [0, 1], [0, 4], [0, 3]]],
    'output': [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0)]
  },
]

# Time Complexity: O((V + E)^2)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    self.graph = graph
    self.path = []
    if not self.is_euler(): return []

    # Find an odd vertex and start traversing from there
    # If there is no odd vertex, start from anywhere (in this case 0)
    odd_vertex = 0
    for node in range(len(graph)):
      if len(graph[node]) % 2 == 1:
        odd_vertex = node
        break

    self.euler_path(odd_vertex)

    return self.path

  def euler_path(self, node):
    for neighbor in self.graph[node]:
      if self.is_valid_next_edge(node, neighbor):
        self.path.append((node, neighbor))
        self.remove_edge(node, neighbor)
        self.euler_path(neighbor)

  def is_valid_next_edge(self, node, neighbor):
    # If neighbor is the only adjacent vertex, then that's the only choice
    if len(self.graph[node]) == 1:
      return True

    # If there are multiple adjacent vertices, we should choose a non-bridge edge.
    # So check if the current edge is a bridge or not.
    # To do so, calculate the number of connected vertices. Then remove the edge, and
    # again calculate the connected vertices. If the the connected vertices reduce, it
    # is a bridge.

    visited = [False] * len(self.graph)
    connected_vertices = self.dfs_count(visited, node)

    self.remove_edge(node, neighbor)

    visited = [False] * len(self.graph)
    connected_vertices_after_removal = self.dfs_count(visited, node)

    self.add_edge(node, neighbor)

    if connected_vertices > connected_vertices_after_removal:
      return False

    return True

  def dfs_count(self, visited, node):
    visited[node] = True
    count = 1

    for neighbor in self.graph[node]:
      if visited[neighbor]: continue
      count += self.dfs_count(visited, neighbor)

    return count

  def add_edge(self, node1, node2):
    self.graph[node1].append(node2)
    self.graph[node2].append(node1)

  def remove_edge(self, node1, node2):
    self.graph[node1].remove(node2)
    self.graph[node2].remove(node1)

  def is_euler(self):
    if not self.is_connected(): return False

    odd_vertices = 0
    for neighbors in self.graph:
      if len(neighbors) % 2 == 1:
        odd_vertices += 1

    if odd_vertices == 0: return True
    # Since an edge requires 2 vertices, there cannot be one odd vertex in a graph
    if odd_vertices == 2: return True
    return False

  def is_connected(self):
    visited = [False] * len(self.graph)
    self.dfs(visited, 0)

    if all(visited): return True
    return False

  def dfs(self, visited, node):
    visited[node] = True

    for neighbor in self.graph[node]:
      if visited[neighbor]: continue
      self.dfs(visited, neighbor)

test_class(Solution, examples)

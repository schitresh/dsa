from utils import test_class

# Given an undirected graph, determine whether the graph contains a
# Hamiltonian cycle or not. If it contains, then print the path.

# Hamiltonian Cycle or Circuit in a graph G is a cycle that visits every vertex of G
# exactly once and returns to the starting vertex. If graph contains a Hamiltonian cycle,
# it is called Hamiltonian graph otherwise it is non-Hamiltonian.
# Finding a Hamiltonian Cycle in a graph is a well-known NP-complete problem, which
# means that there’s no known efficient algorithm to solve it for all types of graphs.
# However, it can be solved for small or specific types of graphs.

# Hamiltonian Path in a graph G is a path that visits every vertex of G exactly once,
# but doesn’t have to return to the starting vertex. It’s an open path.
# Similar to the Hamiltonian Cycle, it is also NP-complete and can be challenging.
# However, it is often more easier than finding a Hamiltonian Cycle.

examples = [
  {
    'input': [[
      [0, 1, 0, 1, 0],
      [1, 0, 1, 1, 1],
      [0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1],
      [0, 1, 1, 1, 0]
    ]],
    'output': [0, 1, 2, 4, 3, 0]
  },
  {
    'input': [[
      [0, 1, 0, 1, 0],
      [1, 0, 1, 1, 1],
      [0, 1, 0, 0, 1],
      [1, 1, 0, 0, 0],
      [0, 1, 1, 0, 0]
    ]],
    'output': None
    # Solution doesn't exist
  },
]

# Time Complexity: O(n!)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, graph):
    self.graph = graph

    for node in range(len(self.graph)):
      self.visited = [False] * len(graph)
      path = self.traverse(node, [])
      if path: return path

  def traverse(self, node, path):
    if self.visited[node]:
      if path[0] == node and all(self.visited):
        path += [node]
        return path
      return

    self.visited[node] = True
    path += [node]

    for neighbor_node in range(len(self.graph)):
      if self.graph[node][neighbor_node] == 0: continue

      new_path = self.traverse(neighbor_node, path)
      if new_path: return new_path

    self.visited[node] = False

test_class(Solution, examples)

# Time Complexity: O(n!)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, graph):
    self.graph = graph
    self.path = [-1] * (len(graph) + 1)
    # Put vertex 0 as the first vertex in the path
    # If there is a hamiltonian cycle, the path can be started from any point
    # of the cycle as the graph is undirected
    self.path[0] = 0
    self.path[-1] = 0

    if self.traverse(1): return self.path

  def traverse(self, pos):
    if pos == len(self.graph):
      first_node = self.path[0]
      last_node = self.path[pos - 1]
      # Last vertex must be adjacent to first vertex to make a cycle
      return self.graph[last_node][first_node] == 1

    for neighbor_node in range(len(self.graph)):
      if not self.is_safe(pos, neighbor_node): continue

      self.path[pos] = neighbor_node
      if self.traverse(pos + 1): return True
      self.path[pos] = -1

    return False

  def is_safe(self, pos, neighbor_node):
    node = self.path[pos -1]
    if self.graph[node][neighbor_node] == 0: return False
    if neighbor_node in self.path: return False

    return True

test_class(Solution2, examples)

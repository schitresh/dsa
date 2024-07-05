from utils import test_class

# Bridges
# An edge in an undirected connected graph is a bridge
# if removing it disconnects the graph
# An edge in an undirected disconnected graph is a bridge
# if removing it increases the number of disconnected components

# Bridges vs Articulation Points
# Articulation points are vertices while bridges are edges
# Removing articulation points increases connected components
# Removing bridges disconnects the graph or increases diconnected components

# Like articulation points, bridges represent vulnerabilities in a connected network
# and are useful for designing reliable networks

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [[2, 4]]
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]],
    'output': [[1, 2], [0, 1], [0, 3]]
  },
  {
    'input': [[[1], [2], [3], []]],
    'output': [[2, 3], [1, 2], [0, 1]]
  },
]

# Tarjan's Algorithm
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Tarjan:
  def __init__(self) -> None:
    self.graph = [[]]
    self.bridges = []
    self.visited = []
    self.disc = []
    self.low = []
    self.parent = []
    self.time = 0

  def solve(self, graph):
    self.graph = graph
    self.bridges = []

    self.visited = [False] * len(graph)
    # Stores discovery times of vertices (When a vertex was visited)
    self.disc = [float('inf')] * len(graph)
    # Stores the earliest visited vertex that can be reached from the subtree rooted at u
    # low[u] = min(disc[u], disc[w]), where w is an ancestor of u
    # And there is a back edge from some descendant of u to w
    # E.g. in 1 -> 2, 2-> 3, 3 -> 1: 3 -> 1 is a back edge
    self.low = [float('inf')] * len(graph)
    self.parent = [-1] * len(graph)

    for node in range(len(graph)):
      if self.visited[node]: continue
      self.dfs(node)

    return self.bridges

  def dfs(self, node):
    self.visited[node] = True
    self.disc[node] = self.time
    self.low[node] = self.time
    self.time += 1

    for neighbor in self.graph[node]:
      if not self.visited[neighbor]:
        self.parent[neighbor] = node

        self.dfs(neighbor)

        # Check if subtree rooted at neighbor
        # has a connection to one of the ancestor of the node
        self.low[node] = min(self.low[node], self.low[neighbor])

        # No need to check for root like articulation points
        # Because edges are independent of children
        # In articualtion point, we check low[neighbor] >= disc[node]
        # But here we check for only greater than
        if self.low[neighbor] > self.disc[node]:
          self.bridges.append([node, neighbor])
      # If the neighbor is already visited and was discovered before the node
      # Then update the low of node to the neighbor's discovery time
      elif neighbor != self.parent[node]:
        self.low[node] = min(self.low[node], self.disc[neighbor])

test_class(Tarjan, examples)

from utils import test_class

# Articulation Points or Cut Vertices
# A vertex V is an articulation point if removing V
# increases the number of connected components

# Connectivity in undirected graph refers to whether two vertices
# are reachable form each other
# If there is a path between two vertices, they are said to be connected

# Articulation points represent vulnerabilities in a connected network,
# single points whose failure would split the network into two or more components
# Useful for designing reliable networks

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [2]
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]],
    'output': [0, 1, 3]
  },
]

# Iterate over all the nodes
# For each node, do DFS traversal excluding that node
# Time Complexity: O(V * (V + E))
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    art_points = []

    # Iterate over all the nodes, the selected node will be excluded in traversal
    for node in range(len(graph)):
      components = 0
      visited = [False] * len(graph)

      # Traverse over the graph excluding the node
      # We need to loop over the vertices because the graph may be disconnected
      for curr in range(len(graph)):
        if curr == node or visited[curr]: continue

        # If the curr is not visited, that means it is a separate component
        # That is, it is disconnected from other graphs
        # Since, the initial value is 0, the first curr is obviously one componnent
        # But after DFS traversal of the first curr, if other vertices are were not visited
        # Then it's a separate component
        components += 1
        self.dfs(graph, visited, node, curr)

      if components > 1:
        art_points.append(node)

    return art_points

  def dfs(self, graph, visited, node, curr):
    visited[curr] = True

    for neighbor in graph[curr]:
      if neighbor == node or visited[neighbor]: continue
      self.dfs(graph, visited, node, neighbor)


# Tarjan's Algorithm
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Tarjan:
  def __init__(self) -> None:
    self.graph = [[]]
    self.art_points = []
    self.visited = []
    self.disc = []
    self.low = []
    self.parent = []
    self.time = 0

  def solve(self, graph):
    self.graph = graph
    self.art_points = []

    self.visited = [0] * len(graph)
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

    return self.art_points

  def dfs(self, node):
    self.visited[node] = True
    self.disc[node] = self.time
    self.low[node] = self.time
    self.time += 1

    # Count of children for the current node
    children = 0

    for neighbor in self.graph[node]:
      if not self.visited[neighbor]:
        self.parent[neighbor] = node
        children += 1

        self.dfs(neighbor)

        # Check if subtree rooted at neighbor
        # has a connection to one of the ancestor of the node
        self.low[node] = min(self.low[node], self.low[neighbor])

        # The node is an articulation point in following cases:
        # (1) The node is the root of DFS tree
        # and has two or more children
        if self.parent[node] == -1:
          if children > 1:
            self.art_points.append(node)
        # (2) The node is not the root
        # and any of its neighbor was discovered after the node
        # That means there is no back edge to any ancestor of node
        # So check if low value of one of its neighbor
        # is more than discovery value of the node
        else:
          if self.low[neighbor] >= self.disc[node]:
            self.art_points.append(node)
      # If the neighbor is already visited and was discovered before the node
      # Then update the low of node to the neighbor's discovery time
      elif neighbor != self.parent[node]:
        self.low[node] = min(self.low[node], self.disc[neighbor])

test_class(Solution, examples)
test_class(Tarjan, examples)

from utils import test_class

# Binconnected Graph
# A graph is said to be biconnected if:
# (1) It is connected, i.e. every vertex can be reached from every other vertex
# (2) Even after removing any vertex, the graph remains connected
# In other words, a connected graph without any articulation point

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': False
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7],
                [3, 4, 6]]],
    'output': False
  },
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2, 4], [2, 3]]],
    'output': True
  },
]

# If there is any articulation point, it is not a biconnected graph
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    self.graph = graph
    self.art_points = []

    self.visited = [False] * len(graph)
    # Stores discovery times of vertices (When a vertex was visited)
    self.disc = [float('inf')] * len(graph)
    # Stores the earliest visited vertex that can be reached from the subtree rooted at u
    # low[u] = min(disc[u], disc[w]), where w is an ancestor of u
    # And there is a back edge from some descendant of u to w
    # E.g. in 1 -> 2, 2-> 3, 3 -> 1: 3 -> 1 is a back edge
    self.low = [float('inf')] * len(graph)
    self.parent = [-1] * len(graph)
    self.time = 0

    if self.any_art_point(0):
      return False

    if not all(self.visited):
      return False

    return True

  def any_art_point(self, node):
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

        if self.any_art_point(neighbor):
          return True

        # Check if subtree rooted at neighbor
        # has a connection to one of the ancestor of the node
        self.low[node] = min(self.low[node], self.low[neighbor])

        # The node is an articulation point in following cases:
        # (1) The node is the root of DFS tree
        # and has two or more children
        if self.parent[node] == -1:
          if children > 1:
            return True
        # (2) The node is not the root
        # and any of its neighbor was discovered after the node
        # That means there is no back edge to any ancestor of the node
        # So check if low value of one of its neighbor is more than discovery value of
        # the node.
        else:
          if self.low[neighbor] >= self.disc[node]:
            return True
      # If the neighbor is already visited and was discovered before the node, then update
      # the low of node to the neighbor's discovery time
      elif neighbor != self.parent[node]:
        self.low[node] = min(self.low[node], self.disc[neighbor])

    return False

test_class(Solution, examples)

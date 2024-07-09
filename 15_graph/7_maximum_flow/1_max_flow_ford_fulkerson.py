from queue import Queue
from utils import test_class

# Maximum Flow Problem
# Finding the maximum amount of flow that can be sent through a network
# of pipes, channels, or other pathways subject to capacity constraints

# There is a directed graph with a source node 's' and a sink node 't'
# Each edge has a capacity thta represents the maximum amount of flow possible
# The goal is to find the max flow that can be sent from s to t

# Can be used in wide variety of real world situations like transportation systems,
# communication networks, resource allocation

examples = [
  {
    'input': [0, 5, [
      [0, 16, 13, 0, 0, 0],
      [0, 0, 10, 12, 0, 0],
      [0, 4, 0, 0, 14, 0],
      [0, 0, 9, 0, 0, 20],
      [0, 0, 0, 7, 0, 4],
      [0, 0, 0, 0, 0, 0]
    ]],
    'output': 23
  }
]

# Ford-Fulkerson Algorithm
# Works by iteratively finding an augmenting path
# Augmenting is a path from the source # to the sink in the residual path
# Residual graph is obtained by subtracting the current flow from the capacity of each edge
# That is, residual capacity = original capacity - current flow
# The algorithm then increases the flow along this path by the maximum possible amount
# DFS only promises to find a path from source to sink, not necessarily a shortest path
# But BFS always finds a shortest path
# Time Complexity: O(V * E^2)
# Auxiliary Space: O(V)
class Solution:
  def solve(self, src, sink, graph):
    # Residual Graph
    self.r_graph = [row.copy() for row in graph]

    max_flow = 0
    # Store parent of the nodes to keep track of the path
    # Helps in retracing the BFS path
    parent = [-1] * len(self.r_graph)

    # Augment the flow while there is still a path from source to sink
    while self.bfs(src, sink, parent):
      path_flow = float('inf')
      node = sink

      while node != src:
        node_parent = parent[node]
        residual_capacity = self.r_graph[node_parent][node]
        # The smallest node will determine how much the flow can pass eventually
        # So path flow should be the minimum residual capacity of the edges
        path_flow = min(path_flow, residual_capacity)
        node = node_parent

      # Add currently determined path flow to the overall flow
      max_flow += path_flow

      # Update residual capacities of the edges and the reverse edges along the path
      # So that the remaining flow can be determined in the next iteration
      node = sink
      while node != src:
        node_parent = parent[node]
        self.r_graph[node_parent][node] -= path_flow
        # Create a back edge (or reverse edge) in case the current path
        # does not end up being a part of the overall flow
        # Consider these paths:
        # s -> a -> c -> t, s -> b -> c -> t, s -> b -> d -> t
        # Suppose s -> b -> c -> t is choosen on the first iteration
        # If we don't add any back edge, we're left with:
        # s -> a -> c, b -> d -> t
        # But in reality, we can also push flow through
        # s -> a -> c -> t and s -> b -> d -> t
        self.r_graph[node][node_parent] += path_flow
        node = node_parent

    return max_flow

  # Checks if there is a path from source to sink
  # Also fills the parent array to store the path
  def bfs(self, src, sink, parent):
    visited = [False] * len(self.r_graph)
    queue = Queue()

    queue.put(src)
    visited[src] = True

    while not queue.empty():
      node = queue.get()

      for neighbor, capacity in enumerate(self.r_graph[node]):
        if visited[neighbor] or capacity == 0: continue

        visited[neighbor] = True
        queue.put(neighbor)
        parent[neighbor] = node

        # If we find a connection to the sink node, then return
        if neighbor == sink: return True

    return False

test_class(Solution, examples)

from queue import Queue
from utils import test_class

# Given a directed path and two vertices s & t, find the maximum number of edge disjoint
# paths from s to t.Two paths are said to be edge disjoint if they don't share any edge.

# This problem can be solved by reducing it to maximum flow problem. Consider the given
# vertices as source and sink in flow network.Assign unit capacity to each edge. Run
# Ford-Fulkerson algorithm to find the maximum flow from source to sink. The maximum
# number of edge disjoint paths is equal to maxium flow.

examples = [
  {
    'input': [0, 7, [
      [0, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]],
    'output': 2
  }
]

# Same as Ford-Fulkerson Algorithm
# Time Complexity: O(V * E^2)
# Auxiliary Space: O(V)
class Solution:
  def solve(self, src, sink, graph):
    # Residual Graph
    self.r_graph = [row.copy() for row in graph]

    max_flow = 0
    # Store parent of the nodes to keep track of the path
    parent = [-1] * len(self.r_graph)

    # Augment the flow while there is still a path from source to sink
    while self.is_path_bfs(src, sink, parent):
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
  def is_path_bfs(self, src, sink, parent):
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

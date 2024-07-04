from queue import Queue
from utils import test_class

# Find the maximum number of edges that can be added to a given DAG
# After which it still remains a DAG
# That is, adding even a single edge will create a cycle in the graph

# If we just want the number without the exact edges, it can be solved like this:
# We can link each node with the maximum number of edges
# This will be (n - 1) + (n -2) + ... + 2 + 1 = N * (N - 1) / 2
# Hence, the max new edges will be: (N * (N - 1) / 2) - E

examples = [
  {
    'input': [[[1, 2, 3], [2], [3, 4], [], []]],
    'output': [[0, 4], [1, 3], [1, 4], [3, 4]]
  },
  {
    'input': [[[1, 2], [2, 3], [3], []]],
    'output': [[0, 3]]
  },
  {
    'input': [[[1], [2], [], [1, 2]]],
    'output': [[0, 3], [0, 2]]
  },
  {
    'input': [[[], [], [3], [1], [0, 1], [0, 2]]],
    'output': [[4, 5], [4, 2], [4, 3], [5, 3], [5, 1], [0, 2], [0, 3], [0, 1], [2, 1]]
  },
]

# Add all the edges in on direction only to avoid making a cycle
# Sort in topological order and create edges from node to all nodes to the right
# This works because to add more edges, we will need to make them from right to left
# but that will surely create a cycle because it's couterpart already has an edge
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    order = self.topological_sort(graph)
    visited = [False] * len(graph)
    new_edges = []

    for i in range(len(order)):
      node = order[i]

      for neighbor in graph[node]:
        visited[neighbor] = True

      for j in range(i + 1, len(order)):
        next_node = order[j]

        if visited[next_node]:
          # Unvisit this node to consider it in further iterations
          visited[next_node] = False
        else:
          new_edges.append([node, next_node])

    return new_edges

  def topological_sort(self, graph):
    in_degree = [0] * len(graph)
    queue = Queue()

    for neighbors in graph:
      for neighbor in neighbors:
        in_degree[neighbor] += 1

    for node in range(len(graph)):
      if in_degree[node] == 0:
        queue.put(node)

    visited = 0
    order = []

    while not queue.empty():
      node = queue.get()
      visited += 1
      order.append(node)

      for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.put(neighbor)

    if visited != len(graph):
      print('Graph contains cycle')
      return

    return order

test_class(Solution, examples)

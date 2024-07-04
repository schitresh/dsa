from queue import LifoQueue, Queue
from utils import test_class

examples = [
  {
    'input': [[[1, 2, 3], [2], [3, 4], [], []]],
    'output': [0, 1, 2, 4, 3]
  },
  {
    'input': [[[1, 2], [2, 3], [3], []]],
    'output': [0, 1, 2, 3]
  },
  {
    'input': [[[1], [2], [], [1, 2]]],
    'output': [3, 0, 1, 2]
  },
  {
    'input': [[[], [], [3], [1], [0, 1], [0, 2]]],
    'output': [5, 4, 2, 3, 1, 0]
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class DfsTopoSort:
  def __init__(self) -> None:
    self.graph = [[]]
    self.stack = []
    self.visited = []

  def solve(self, graph):
    self.graph = graph
    self.stack = LifoQueue()
    self.visited = [False] * len(graph)

    # Iterate over all the nodes in case the graph is disconnected
    for node in range(len(graph)):
      if self.visited[node]: continue
      self.dfs(node)

    return self.stack_array()

  def dfs(self, node):
    self.visited[node] = True

    for neighbor in self.graph[node]:
      if self.visited[neighbor]: continue
      self.dfs(neighbor)

    # Put the current node only after all the nodes are visited
    # This way all the directed neighbors will be at the bottom of the stack
    # And while popping the source will always be the first
    self.stack.put(node)

  def stack_array(self):
    return list(reversed(self.stack.queue))

# Kahn's Algorithm
# Uses BFS and works by repeatedly finding vertices with no incoming edges
# That is, in-degree of the node is 0
# Removing them from the graph and updating the incoming edges of remaining vertices
# This is because when the in-degree is 0,
# all the sources of that node has been visited
# and hence can be added to the order
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class BfsTopoSort:
  def solve(self, graph):
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

test_class(DfsTopoSort, examples)
test_class(BfsTopoSort, examples)

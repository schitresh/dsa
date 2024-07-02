from queue import LifoQueue, Queue
from utils import test_class, test_with_init

examples = [
  {
    'input': [[[1], [0, 2], [1, 3, 4], [2], [2]]],
    'output': False
  },
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': True
  },
]

# Track the current path in recursion stack
# If the node appears again in the recursion stack, then there is a cycle
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class DFSRecursive:
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.recursion_stack = [False] * len(graph)

  def traverse(self, node, parent):
    self.visited[node] = True

    for neighbor in self.graph[node]:
      if not self.visited[neighbor]:
        if self.traverse(neighbor, node):
          return True
      # If the neighbor is visited and not parent, then there is a cycle
      elif neighbor != parent:
        return True

    # Pop the current node from the recursion stack
    # Since the current path is traversed
    self.recursion_stack[node] = False
    return False

  def solve(self):
    for current in range(len(self.graph)):
      if self.visited[current]: continue
      if self.traverse(current, -1): return True

    return False

test_with_init(DFSRecursive, examples)
test_with_init(DFSColors, examples)
test_class(TopologicalSorting, examples)

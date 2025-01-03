from utils import test_class

# Given an undirected graph, check if there is a cycle in the given graph.

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

# Using Recursive DFS
# Track the current path in recursion stack
# If the node appears again in the recursion stack, then there is a cycle
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)

    for current in range(len(graph)):
      if self.visited[current]: continue
      if self.traverse(current, -1): return True

    return False

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
    return False

test_class(Solution, examples)

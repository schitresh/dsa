from utils import test_class

# Given a graph, a source vertex in the graph and a number k, find if there is a
# simple path (without any cycle) starting from the given source and ending at any other
# vertex such that the distance from source to that vertex is atleast k length.

examples = [
  {
    'input': [0, 58, [
      [[1, 4], [7, 8]],
      [[0, 4], [2, 8], [7, 11]],
      [[1, 8], [3, 7], [5, 4], [8, 2]],
      [[2, 7], [4, 9], [5, 14]],
      [[3, 9], [5, 10]],
      [[2, 4], [3, 14], [4, 10], [6, 2]],
      [[5, 2], [7, 1], [8, 6]],
      [[0, 8], [1, 11], [6, 1], [8, 7]],
      [[2, 2], [6, 6], [7, 7]],
    ]], # Src, k, Ajacency list
    'output': True
  },
  {
    'input': [0, 62, [
      [[1, 4], [7, 8]],
      [[0, 4], [2, 8], [7, 11]],
      [[1, 8], [3, 7], [5, 4], [8, 2]],
      [[2, 7], [4, 9], [5, 14]],
      [[3, 9], [5, 10]],
      [[2, 4], [3, 14], [4, 10], [6, 2]],
      [[5, 2], [7, 1], [8, 6]],
      [[0, 8], [1, 11], [6, 1], [8, 7]],
      [[2, 2], [6, 6], [7, 7]],
    ]], # Src, k, Ajacency list
    'output': False
  },
]

# Backtracking
# Time Complexity: O((n - 1)!)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, src, limit, graph):
    self.src = src
    self.limit = limit
    self.graph = graph
    self.visited = [False] * len(graph)
    return self.traverse(src, 0)

  def traverse(self, node, cost):
    if cost >= self.limit: return True

    self.visited[node] = True

    for neighbor, neighbor_cost in self.graph[node]:
      if self.visited[neighbor]: continue
      result = self.traverse(neighbor, cost + neighbor_cost)
      if result: return True

    self.visited[node] = False

    return False

test_class(Solution, examples)

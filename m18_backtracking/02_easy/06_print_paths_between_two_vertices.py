from utils import test_class

# Given a directed graph, a source vertex 's' and a destination vertex 'd', print all
# paths from 's' to 'd'.

examples = [
  {
    'input': [0, 4, [[1, 2, 4], [3, 4], [4], [2], []]], # Src, Dest, Ajacency list
    'output': [[0, 4], [0, 2, 4], [0, 1, 4], [0, 1, 3, 2, 4]]
  },
  {
    'input': [0, 2, [[1, 2, 4], [3, 4], [4], [2], []]], # Src, Dest, Ajacency list
    'output': [[0, 2], [0, 1, 3, 2]]
  },
  {
    'input': [0, 4, [[1, 2, 4], [3, 4], [1, 4], [2], []]], # Src, Dest, Ajacency list
    'output': [[0, 4], [0, 2, 4], [0, 2, 1, 4], [0, 1, 4], [0, 1, 3, 2, 4], ]
  },
  {
    'input': [2, 3, [[1, 2, 3], [3], [0, 1], []]], # Src, Dest, Ajacency list
    'output': [[2, 1, 3], [2, 0, 3], [2, 0, 1, 3]]
  },
]

# Backtracking
# Time Complexity: O((v - 1)!)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, src, dest, graph):
    self.src = src
    self.dest = dest
    self.graph = graph

    self.visited = [False] * len(graph)
    self.paths = []

    self.traverse(src, [src])
    return self.paths

  def traverse(self, node, path):
    if node == self.dest:
      self.paths.append(path.copy())

    self.visited[node] = True

    for neighbor in reversed(self.graph[node]):
      if self.visited[neighbor]: continue
      self.traverse(neighbor, path + [neighbor])

    self.visited[node] = False

test_class(Solution, examples)

from utils import test_class

# Count the total number of ways or paths that exist between two vertices in a directed
# graph. Do not consider an addition of cycle as another path.

examples = [
  {
    'input': [0, 4, [[1, 2, 4], [3, 4], [4], [2], []]], # Src, Dest, Ajacency list
    'output': 4
    # 0 -> 4
    # 0 -> 1 -> 4
    # 0 -> 2 -> 4
    # 0 -> 1 -> 3 -> 2 -> 4
  },
  {
    'input': [0, 2, [[1, 2, 4], [3, 4], [4], [2], []]], # Src, Dest, Ajacency list
    'output': 2
    # 0 -> 2
    # 0 -> 1 -> 3 -> 2
  },
  {
    'input': [0, 4, [[1, 2, 4], [3, 4], [1, 4], [2], []]], # Src, Dest, Ajacency list
    'output': 5
    # Additional path: 0 -> 2 -> 1 -> 4
  },
]

# Backtracking
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, src, dest, graph):
    self.src = src
    self.dest = dest
    self.graph = graph
    self.visited = [False] * len(graph)
    return self.traverse(src)

  def traverse(self, node):
    if node == self.dest: return 1

    self.visited[node] = True
    paths = 0

    for neighbor in self.graph[node]:
      if self.visited[neighbor]: continue
      paths += self.traverse(neighbor)

    self.visited[node] = False

    return paths

test_class(Solution, examples)

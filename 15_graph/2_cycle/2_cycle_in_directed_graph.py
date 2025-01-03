from queue import Queue
from utils import test_class

examples = [
  {
    'input': [[[1, 2], [2], [3], []]],
    'output': False
  },
  {
    'input': [[[1, 2], [2], [0, 3], []]],
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
    self.recursion_stack = [False] * len(graph)

    for current in range(len(graph)):
      if self.visited[current]: continue
      if self.traverse(current): return True

    return False

  def traverse(self, node):
    # Add the current node to the recusion stack
    self.recursion_stack[node] = True
    self.visited[node] = True

    for neighbor in self.graph[node]:
      if not self.visited[neighbor]:
        if self.traverse(neighbor):
          return True
      elif self.recursion_stack[neighbor]:
        return True

    # Pop the current node from the recursion stack
    # Since the current path is traversed
    self.recursion_stack[node] = False
    return False

test_class(Solution, examples)

# Color Coding
# Use color codes to track status
# White: Vertex is not processed yet, all vertices are white initially
# Grey: Vertex is being processed, DFS has started but not finished
# If there is an edge from the current vertex to a grey vertex, then there is a cycle
# Black: Vertex is processed
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution2:
  def solve(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.color = ['white'] * len(graph)

    for current in range(len(graph)):
      if self.color[current] == 'white':
        if self.traverse(current):
          return True

    return False

  def traverse(self, node):
    self.color[node] = 'grey'

    for neighbor in self.graph[node]:
      if self.color[neighbor] == 'white':
        if self.traverse(neighbor):
          return True
      elif self.color[neighbor] == 'grey':
        return True

    self.color[node] = 'black'
    return False

test_class(Solution2, examples)

# Using Kahn's Algorithm (For Topological Sorting)
# If it successfully removes all vertices from the graph, then it's a DAG
# (Directed Acyclic Graph).
# If there are remaining vertices with indegrees greater than 1, then there's at least
# one cycle
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution3:
  def solve(self, graph):
    in_degree = [0] * len(graph)
    queue = Queue()
    visited = 0

    # Calculate in_degree for each vertex
    for node in range(len(graph)):
      for neighbor in graph[node]:
        in_degree[neighbor] += 1

    # Enqueue vertices with 0 in-degree
    for node in range(len(graph)):
      if in_degree[node] == 0:
        queue.put(node)

    # BFS Traversal
    while not queue.empty():
      node = queue.get()
      visited += 1

      for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.put(neighbor)

    return visited != len(graph)

test_class(Solution3, examples)

# Disjoing Set
# Time Complexity: O(E * log(V))
# Auxiliary Space: O(V)
class Solution4:
  def solve(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.parent = [i for i in range(len(graph))]
    self.rank = [False] * len(graph)

    for current in range(len(graph)):
      curr_rep = self.find(current)

      for neighbor in graph[current]:
        neighbor_rep = self.find(neighbor)
        if curr_rep == neighbor_rep: return True

        self.union(curr_rep, neighbor_rep)

    return False

  def find(self, node):
    parent = self.parent[node]
    if parent != node:
      self.parent[node] = self.find(parent)

    return self.parent[node]

  def union(self, i_rep, j_rep):
    i_rank = self.rank[i_rep]
    j_rank = self.rank[j_rep]

    if i_rank < j_rank:
      self.parent[i_rep] = j_rep
    elif i_rank > j_rank:
      self.parent[j_rep] = i_rep
    else:
      self.parent[i_rep] = j_rep
      self.rank[j_rep] += 1

test_class(Solution4, examples)

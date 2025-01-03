from utils import test_class

# Given an undirected and connected graph and a number n, count the total number of
# simple cycles of length n in the graph. A simple cycle of length n is defined as a
# cycle that contains exactly n vertices and n edges.
# For an undirected graph, each cycle should only be counted once, regardless of
# starting vertex or direction.

examples = [
  {
    'input': [[[1, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3]], 4],
    'output': 3
  },
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]], 4],
    'output': 1
  },
]

# DFS
# Track the current path in recursion stack
# If the node appears again in the recursion stack, then there is a cycle
# Time Complexity: O(V^2)
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph, cycle_len):
    self.graph = graph
    self.cycle_len = cycle_len
    self.visited = [False] * len(graph)
    self.count = 0

    for current in range(len(self.graph)):
      self.traverse(current, current, 1)
      # Every traverse call marks a node unvisited to consider different paths
      # Hence, mark the current node visited after traversing is finished
      self.visited[current] = True

    # Every cycle will be counted twice
    # Because one path will be clockwise and another would be couter-clockwise
    # And both will be considered while iterating through neighbors of a node
    return self.count // 2

  def traverse(self, start_node, curr_node, curr_len):
    self.visited[curr_node] = True

    # If we have iterated N nodes, check if there is a cycle
    if curr_len == self.cycle_len:
      # If the current node (after n iterations) connects to the start node
      # Then there is a cycle oif length N
      if start_node in self.graph[curr_node]:
        self.count += 1

      # Mark the current node un-visited to check cycles for other starting nodes
      self.visited[curr_node] = False
      return

    for neighbor in self.graph[curr_node]:
      if not self.visited[neighbor]:
        self.traverse(start_node, neighbor, curr_len + 1)

    # Mark the current node un-visited to check cycles for other starting nodes
    self.visited[curr_node] = False

test_class(Solution, examples)

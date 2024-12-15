from utils import test_class

# Every house in a colony has at most one pipe going into it
# and at most one pipe going out of it
# Tanks and taps are to be installed such that
# every house with one outgoing pipe but no incoming pipe gets a tank installed
# And every house with only an incoming pipe and no outgoing pipe gets a tap

# Given the number of houses and the number of pipes
# The connections of pipe among the houses contain three input values: a, b, d
# denoting the pipe of diameter d from house a to house b

# Find out the efficient solution for the network
# The output will contain the number of pairs of tanks and taps installed in the first line
# The next t lines contain three integers:
# house number of tank, house number of tap and the minimum diameter of pipe between them

examples = [
  {
    'input': [
      4, 2,
      [[1, 2, 60], [3, 4, 50]]
    ],
    'output': [2, [[1, 2, 60], [3, 4, 50]]],
  },
  {
    'input': [
      9, 6,
      [[7, 4, 98], [5, 9, 72], [4, 6, 10 ], [2, 8, 22], [9, 7, 17], [3, 1, 66]]
    ],
    'output': [3, [[2, 8, 22], [3, 1, 66], [5, 6, 10]]],
  },
]

# Start from the tank houses, i.e. the house with only outgoing pipe
# Apply DFS on these tank houses to reach the tap houses,
# i.e. the house with only incoming pipe
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, house_count, pipe_count, pipes):
    # Stores corresponding end house for the start house as index
    self.end_house = [0] * (house_count + 1)
    # Stores corresponding start house for the end house as index
    self.start_house = [0] * (house_count + 1)
    # Diameter of pipe starting at the start house as index
    self.diameter_start_house = [0] * (house_count + 1)

    result = []

    for pipe in pipes:
      from_house, to_house, diameter = pipe
      self.end_house[from_house] = to_house
      self.start_house[to_house] = from_house
      self.diameter_start_house[from_house] = diameter

    for tank_house in range(1, house_count + 1):
      # If the house has no incoming pipe but, but an outgoing pipe is present
      # then it is a tank. Apply DFS to reach the end point of this path, that is,
      # the house where there is only one incoming pipe and no outgoing pipe,
      # which will be the tap house.
      if self.start_house[tank_house] == 0 and self.end_house[tank_house]:
        tap_house, min_diameter = self.dfs(tank_house, float('inf'))
        result.append([tank_house, tap_house, min_diameter])

    return [len(result), result]

  def dfs(self, house, min_diameter):
    end_house = self.end_house[house]
    diameter = self.diameter_start_house[house]

    if end_house == 0:
      return [house, min_diameter]

    min_diameter = min(min_diameter, diameter)
    return self.dfs(end_house, min_diameter)

test_class(Solution, examples)

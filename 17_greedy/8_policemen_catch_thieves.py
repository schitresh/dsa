from utils import test_class

# Given an array such that:
# - Each element in the array contains either a policeman or a thief
# - Each policeman can catch only one thief
# - A policeman cannot catch a thief who is more than K units away from the policeman
# Find the maximum number of thieves that can be caught

examples = [
  {
    'input': [['P', 'T', 'T', 'P', 'T'], 1],
    'output': 2
  },
  {
    'input': [['T', 'T', 'P', 'P', 'T', 'P'], 2],
    'output': 3
  },
  {
    'input': [['P', 'T', 'P', 'T', 'T', 'P'], 3],
    'output': 3
  },
]

# Brute force approach: Check all feasible sets of combinations of a police & a thief
# Greedy approaches:
# Approach 1: For each policeman, catch the nearest possible thief
# This works for example 1, but fails for example 2
# Approach 2: For each policeman, catch the farthest possible thief
# This works for example 2, but fails for example 3
# Approach 3: Focusing on just the allotment
# Get the lowest index of policemen & thief
# Make an allotment if |p - t| < k and increment to the next p & t
# Otherwise increment min(p, t) to the next p or t
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array, max_dist):
    max_theives_caught = 0
    policemen = []
    thieves = []

    for i in range(len(array)):
      if array[i] == 'P': policemen.append(i)
      elif array[i] == 'T': thieves.append(i)

    police = 0
    thief = 0
    while police < len(policemen) and thief < len(thieves):
      if abs(policemen[police] - thieves[thief]) <= max_dist:
        max_theives_caught += 1
        police += 1
        thief += 1
      elif policemen[police] < thieves[thief]:
        police += 1
      else:
        thief += 1

    return max_theives_caught

# In the previous solution, directly calculate the next index fo police & thief
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array, max_dist):
    max_theives_caught = 0
    police = self.find_next_police(array, -1)
    thief = self.find_next_thief(array, -1)

    while police != -1 and thief != -1:
      if abs(police - thief) <= max_dist:
        max_theives_caught += 1
        police = self.find_next_police(array, police)
        thief = self.find_next_thief(array, thief)
      elif police < thief:
        police = self.find_next_police(array, police)
      else:
        thief = self.find_next_thief(array, thief)

    return max_theives_caught

  def find_next_police(self, array, curr):
    for i in range(curr + 1, len(array)):
      if array[i] == 'P':
        return i

    return -1

  def find_next_thief(self, array, curr):
    for i in range(curr + 1, len(array)):
      if array[i] == 'T':
        return i

    return -1

test_class(Solution, examples)
test_class(Solution2, examples)

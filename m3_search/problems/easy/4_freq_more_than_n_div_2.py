from utils import test_class

# Given an array of size n, find the majority element. The majority element is the one
# that occurs more than n/2 times in the array.

examples = [
  {
    'input': [[2, 1, 3, 1, 5, 1, 1]],
    'output': 1,
  },
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': None,
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    counts = {}

    for num in array:
      counts[num] = counts.get(num, 0) + 1

    for key, value in counts.items():
      if value > len(array) // 2:
        return key

    return None

test_class(Solution, examples)

# Moore's Voting Algorithm
# The first element is choosen as a candidate with 1 vote. While iterating the array,
# we keep incrementing the vote count if the elements are equal to the candidate, else
# the vote count is decremented.
# This means that we are decreasing the priority of winning ability of the selected
# candidate, since we know that if the candidate is in majority it occurs more than N/2\
# times and the remaining elements are occur less than N/2 times.
# If the votes become 0, then there are the equal number of votes for different elements.
# So the candidate cannot be the majority and hence we choose the present element as the
# candidate and continue.
# The final candidate can be the majority element. To check that, calculate the count of
# the candidate in the array and confirm that its greater than N/2.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    candidate = -1
    votes = 0

    for num in array:
      if votes == 0:
        candidate = num
        votes = 1
      elif num == candidate:
        votes += 1
      else:
        votes -= 1

    count = 0
    for num in array:
      if num == candidate:
        count += 1

    if count > len(array) // 2: return candidate
    return None

test_class(Solution2, examples)

from collections import Counter
from utils import test_class

# Given an array of size n and an integer k, find all elements in the array that appear
# more than n/k times.

examples = [
  {
    'input': [[3, 1, 2, 2, 1, 2, 3, 3], 4],
    'output': [3, 2],
  },
  {
    'input': [[9, 8, 7, 9, 2, 9, 7], 3],
    'output': [9],
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array, k):
    target_count = len(array) // k
    result = []
    counts = {}

    for num in array:
      counts[num] = counts.get(num, 0) + 1

    for key, value in counts.items():
      if value > target_count:
        result.append(key)

    return result

test_class(Solution, examples)

# Moore's Voting Algorithm
# There can be at max k – 1 elements present in the array which appears more than n/k
# times. When we encounter an element which is one of our candidates then increment the
# vote else decrement the vote.
# Let's say we have m elements which have count > n/k, then the frequency of these
# elements is m * (n / k). Let's say the count of remaining elements is x. Then,
# m * (n / k) + x = n. That implies that m * (n / k) < n, which simplifies to m < k.
# Hence, there can be at max k - 1 such elements.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array, k):
    votes = {}

    for num in array:
      if num in votes:
        votes[num] += 1
      elif len(votes) < k - 1:
        votes[num] = 1
      # Since there can be at max k - 1 elements that appear more than n/k times,
      # we need to remove elements which are weak candidates. To do this, decrement
      # votes of each key by 1 to bring them equal to the current num. If the vote
      # drops to 0, remove the key.
      else:
        to_remove = []

        for key in votes:
          votes[key] -= 1
          if votes[key] == 0:
            to_remove.append(key)

        for key in to_remove:
          del votes[key]

    result = []

    for candidate in votes:
      count = 0
      for num in array:
        if num == candidate:
          count += 1

      if count > len(array) // k:
        result.append(candidate)

    return result

test_class(Solution2, examples)

# Moore's Voting Algorithm with Counter class
# Time Complexity: O(n * k)
# Auxiliary Space: O(k)
class Solution3:
  def solve(self, array, k):
    votes = {}

    for num in array:
      if num in votes:
        votes[num] += 1
      elif len(votes) < k - 1:
        votes[num] = 1
      # Since there can be at max k - 1 elements that appear more than n/k times,
      # we need to remove elements which are weak candidates. To do this, decrement
      # votes of each key by 1 to bring them equal to the current num. If the vote
      # drops to 0, remove the key.
      else:
        to_remove = []

        for key in votes:
          votes[key] -= 1
          if votes[key] == 0:
            to_remove.append(key)

        for key in to_remove:
          del votes[key]

    result = []

    counts = Counter(array)
    result = [key for key, value in counts.items() if value > len(array) // k]
    return result

test_class(Solution2, examples)

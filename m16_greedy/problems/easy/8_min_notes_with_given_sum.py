from collections import defaultdict
from utils import test_class

# Given an amount, find the minimum number of notes of different denominations that
# sum up to the given amount. Starting from the highest denomination note, try to
# accommodate as many notes as possible for a given amount. We may assume that we have
# infinite supply of notes of values {2000, 500, 200, 100, 50, 20, 10, 5, 1}

examples = [
  {
    'input': [800],
    'output': {500: 1, 200: 1, 100: 1},
  },
  {
    'input': [2456],
    'output': {2000: 1, 200: 2, 50: 1, 5: 1, 1: 1},
  }
]

# Time Complexity: O(1)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    notes = {}

    for note in denominations:
      if amount >= note:
        notes[note] = amount // note
        amount = amount % note

    return notes

test_class(Solution, examples)

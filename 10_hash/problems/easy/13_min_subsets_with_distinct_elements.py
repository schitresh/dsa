from utils import test_class

# Given an array, make minimum number of subsets such that no subset contain duplicate
# elements.

examples = [
  {
    'input': [[1, 2, 3, 4]],
    'output': 1,
    # A single subset can contain all the values without duplicates
  },
  {
    'input': [[1, 2, 3, 3]],
    'output': 2,
    # Create two subsets: [1, 2, 3] & [3] (or [1, 3], [2, 3])
  },
  {
    'input': [[1, 2, 1, 2, 3, 3, 2, 2]],
    'output': 4,
    # [1, 2, 3], [1, 2, 3], [2], [2]
  },
]

# Brute Force
# The result is equal to the frequency of the most frequent element. Since we have to
# create a subset such that each element in a subset is unique that means that all the
# repeating elements should be kept in a different set. Hence the maximum subsets
# required is the frequency of the element occurring maximum time.
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    max_freq = 0

    for item in array:
      freq = 0
      for item2 in array:
        if item == item2: freq += 1

      max_freq = max(max_freq, freq)

    return max_freq

test_class(Solution, examples)

# Brute Force with Sorting
# If we sort the array, we can calculate frequency of each element in single iteration
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    array.sort()
    max_freq = 0
    freq = 1

    for i in range(1, len(array)):
      if array[i] == array[i - 1]:
        freq += 1
      else:
        max_freq = max(max_freq, freq)
        freq = 1

    # Since the loop will exit after the last element without calculating max freq
    max_freq = max(max_freq, freq)
    return max_freq

test_class(Solution2, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, array):
    freq = {}

    for item in array:
      freq[item] = freq.get(item, 0) + 1

    subset_count = 0
    while True:
      empty = True

      for item in list(freq.keys()):
        if freq[item] > 0:
          freq[item] -= 1
          empty = False

      if empty: break
      subset_count += 1

    return subset_count

test_class(Solution3, examples)

# Hashing with max frequency
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, array):
    freq = {}

    for item in array:
      freq[item] = freq.get(item, 0) + 1

    return max(freq.values())

test_class(Solution4, examples)

# Hashset of unique items
# Initialize a hash set to store distinct elements. For each element, check if it is
# already present in the hash set. If the element is not present, add it to the hash
# set. If the element is present, increment the count and reset the hash set.
# Finally, return the count.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution5:
  def solve(self, array):
    unique_items = set()
    count = 0

    for item in array:
      if item not in unique_items:
        unique_items.add(item)
      else:
        count += 1
        unique_items.clear()
        unique_items.add(item)

    if len(unique_items) > 0: count += 1
    return count

test_class(Solution5, examples)

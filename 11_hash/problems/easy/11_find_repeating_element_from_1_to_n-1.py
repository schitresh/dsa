from utils import test_class

# In an array of size n filled with numbers from 1 to n-1 in random order, there is only
# one repetitive element. Find the repetitive element.

examples = [
  {
    'input': [[1, 3, 2, 3, 4]],
    'output': 3,
  },
  {
    'input': [[1, 5, 1, 2, 3, 4]],
    'output': 1,
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    array.sort()

    for i in range(len(array) - 1):
      if array[i] == array[i + 1]: return array[i]

    return None

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    hash_set = set()

    for item in array:
      if item in hash_set: return item
      hash_set.add(item)

    return None

test_class(Solution2, examples)

# Sum Formula
# The sum of number from 1 to k is k * (k + 1) / 2
# If we sum the number and subtract the result of this formula, we get the element
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    k = len(array) - 1
    expected_sum = k * (k + 1) // 2
    array_sum = sum(array)
    return array_sum - expected_sum

test_class(Solution3, examples)

# XOR
# xor(x, x) = 0 and if xor(x, y) = z, then xor(x, z) = y
# So, xor elements from 1 to n - 1, then xor elements of the array
# THe xor of these two results would be the answer
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, array):
    elements_xor = 0
    array_xor = 0

    for i in range(len(array)):
      elements_xor ^= i

    for item in array:
      array_xor ^= item

    return elements_xor ^ array_xor

test_class(Solution4, examples)

# Using elements as indexes
# Since numbers are from 1 to (n - 1), we can make the value negative for indexes as we
# iterate the array. The duplicate element will be already be negative.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution5:
  def solve(self, array):
    for item in array:
      val = abs(item)
      if array[val] < 0: return val
      array[val] *= -1

test_class(Solution5, examples)

# Floyd Cycle Detection
# Use two pointers, fast and slow. The fast one goes forward two steps each time, while
# the slow one goes only one step each time. They must have met the duplicate item if
# slow == fast. In fact, they meet in a circle, the duplicate number must be the entry
# point of the circle when visiting the array from array[0].
# Next we just need to find the entry point. We use a point (we can use the fast one
# before) to visit from the beginning with one step each time, do the same job to slow.
# When fast == slow, they meet at the entry point of the circle.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution6:
  def solve(self, array):
    slow = array[0]
    fast = array[0]

    while True:
      slow = array[slow]
      fast = array[array[fast]]

      if slow == fast: break

    fast = array[0]
    while slow != fast:
      slow = array[slow]
      fast = array[fast]

    return slow

test_class(Solution6, examples)

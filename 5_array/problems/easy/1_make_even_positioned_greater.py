from utils import test_class

# Rearrange array such that even positioned elements are greater than the odd ones.
# Considering 1-based indexing,
# If i is even: arr[i] >= arr[i – 1]
# If i is odd: arr[i] <= arr[i – 1]

examples = [
  {
    'input': [[1, 2, 2, 1]],
    'output': [1, 2, 1, 2],
  },
  {
    'input': [[1, 3, 2]],
    'output': [1, 3, 2],
  },
  {
    'input': [[1, 2, 3, 4, 5, 6]],
    'output': [1, 6, 2, 5, 3, 4], # or, [1, 3, 2, 5, 4, 6]
  },
  {
    'input': [[6, 5, 4, 3, 2, 1]],
    'output': [1, 6, 2, 5, 3, 4], # or, [5, 6, 3, 4, 1, 2]
  }
]

# Sorting
# Assign the n/2 largest elements to even positions and the rest to odd positions
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    array.sort()
    result = []
    left = 0
    right = len(array) - 1

    for i in range(len(array)):
      if (i + 1) % 2 == 0:
        result.append(array[right])
        right -= 1
      else:
        result.append(array[left])
        left += 1

    return result

test_class(Solution, examples)

# Swapping
# For every i, check the specified condition for i & i - 1 (based on i is even or odd)
# If not satisfied, swap the elements at i & i - 1
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    for i in range(1, len(array)):
      if (i + 1) % 2 == 0:
        if array[i - 1] > array[i]:
          array[i - 1], array[i] = array[i], array[i - 1]
      else:
        if array[i - 1] < array[i]:
          array[i - 1], array[i] = array[i], array[i - 1]

    return array

test_class(Solution2, examples)

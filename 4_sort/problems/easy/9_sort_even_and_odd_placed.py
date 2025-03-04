from utils import test_class

# Given an array of n distinct numbers, sort all even-placed numbers in increasing and
# odd-placed numbers in decreasing order. The modified array should contain all sorted
# even-placed numbers followed by reverse sorted odd-placed numbers.
# Note that the first element is considered as even placed because of its index 0.

examples = [
  {
    'input': [[0, 1, 2, 3, 4, 5, 6, 7]],
    'output': [0, 2, 4, 6, 7, 5, 3, 1],
    # Even-placed elements: 0, 2, 4, 6
    # Odd-placed elements: 1, 3, 5, 7
    # Even-placed elements in increasing order: 0, 2, 4, 6
    # Odd-Placed elements in decreasing order: 7, 5, 3, 1
  },
  {
    'input': [[3, 1, 2, 4, 5, 9, 13, 14, 12]],
    'output': [2, 3, 5, 12, 13, 14, 9, 4, 1],
  },
]

# Auxiliary Arrays
# Create auxiliary arrays for even placed & odd placed elements and sort them each
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    even_placed_nums = []
    odd_placed_nums = []

    for i in range(len(array)):
      if i % 2 == 0:
        even_placed_nums.append(array[i])
      else:
        odd_placed_nums.append(array[i])

    even_placed_nums.sort()
    odd_placed_nums.sort(reverse = True)

    idx = 0
    for num in even_placed_nums:
      array[idx] = num
      idx += 1

    for num in odd_placed_nums:
      array[idx] = num
      idx += 1

    return array

test_class(Solution, examples)

class MergeSort:
  def sort(self, array, left, right, reverse = False):
    if left >= right: return
    mid = left + (right - left) // 2
    self.sort(array, left, mid, reverse = reverse)
    self.sort(array, mid + 1, right, reverse = reverse)
    self.merge(array, left, mid, right, reverse = reverse)

  def merge(self, array, left, mid, right, reverse = False):
    low = left
    high = mid + 1
    temp = []

    while low <= mid and high <= right:
      if array[low] <= array[high]:
        if reverse:
          temp.append(array[high])
          high += 1
        else:
          temp.append(array[low])
          low += 1
      else:
        if reverse:
          temp.append(array[low])
          low += 1
        else:
          temp.append(array[high])
          high += 1

    while low <= mid:
      temp.append(array[low])
      low += 1

    while high <= right:
      temp.append(array[high])
      high += 1

    for i in range(len(temp)):
      array[left + i] = temp[i]

# Partition
# Move all the even positioned elements to the left partition and odd positioned
# elements to the right partition within the array. Then sort the even and odd part
# seperately in increasing & decreasing order respectively.
# To do this, swap each even indexed element with elements in the first partition of the
# array
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    even_index_count = len(array) // 2
    if len(array) % 2 == 1: even_index_count += 1

    even_i = 0
    for i in range(even_index_count):
      array[i], array[even_i] = array[even_i], array[i]
      even_i += 2

    # Using library sort will require additional space because array[0:even_index_count]
    # will generate a new array, so using merge sort
    MergeSort().sort(array, 0, even_index_count - 1)
    MergeSort().sort(array, even_index_count, len(array) - 1, reverse = True)

    return array

test_class(Solution2, examples)

# Partition
# Partition same as above, but in a different way. Swap first half of odd indexed
# elements with the second half of even indexed elements.
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    odd_idx = 1
    even_idx = len(array) - 1
    if even_idx % 2 == 1: even_idx -= 1

    while odd_idx < even_idx:
      array[odd_idx], array[even_idx] = array[even_idx], array[odd_idx]
      odd_idx += 2
      even_idx -= 2


    even_index_count = (len(array) + 1) // 2
    # Using library sort will require additional space because array[0:even_index_count]
    # will generate a new array, so using merge sort
    MergeSort().sort(array, 0, even_index_count - 1)
    MergeSort().sort(array, even_index_count, len(array) - 1, reverse = True)

    return array

test_class(Solution3, examples)

# Negative Multiplication
# Multiply all even indexed elements by -1 and sort the whole array. Then revert the
# signs for the even elements. Reverse the both the halves separately to get
# increasing order for even indexed elements and decreasing order for odd indexed
# elements.
# decreasing order.
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, array):
    for i in range(0, len(array), 2):
      array[i] *= -1

    array.sort()

    even_index_count = (len(array) + 1) // 2
    for i in range(even_index_count):
      array[i] *= -1

    self.reverse(array, 0, even_index_count - 1)
    self.reverse(array, even_index_count, len(array) - 1)
    return array

  def reverse(self, array, left, right):
    while left < right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1

    return array

test_class(Solution4, examples)

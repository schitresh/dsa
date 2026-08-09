from utils import test_class

# Given an array of positive integers, sort the array in decreasing order of count of
# set bits in binary representations of array elements. For integers having the same
# number of set bits, sort according to their position in the original array i.e. a
# stable sort.

examples = [
  {
    'input': [[5, 2, 3, 9, 4, 6, 7, 15, 32]],
    'output': [15, 7, 5, 3, 9, 6, 2, 4, 32],
  },
  {
    'input': [[1, 2, 3, 4, 5, 6]],
    'output': [3, 5, 6, 1, 2, 4],
  },
]

# Insertion Sort
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    bit_counts = [0] * len(array)
    for i in range(len(array)):
      bit_counts[i] = self.count_set_bits(array[i])

    self.insertion_sort(array, bit_counts)

    return array

  def count_set_bits(self, num):
    count = 0
    while num:
      if num & 1 == 1: count += 1
      num >>= 1

    return count

  def insertion_sort(self, array, bit_counts):
    for i in range(1, len(array)):
      bit_count = bit_counts[i]
      num = array[i]
      j = i

      while j > 0 and bit_counts[j - 1] < bit_count:
        bit_counts[j] = bit_counts[j - 1]
        array[j] = array[j - 1]
        j -= 1

      bit_counts[j] = bit_count
      array[j] = num

test_class(Solution, examples)

# Library Sort
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    array.sort(key = self.count_set_bits, reverse = True)
    return array

  def count_set_bits(self, num):
    count = 0
    while num:
      if num & 1 == 1: count += 1
      num >>= 1

    return count

test_class(Solution2, examples)

# Counting Sort
# Assuming that an integer takes 32 bits, there can be a minimum 1 set bit and a maximum
# of 31 set bits in an integer
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, array):
    max_bit_len = 32
    bit_count_nums = [[] for _ in range(max_bit_len)]

    for num in array:
      set_bits = self.count_set_bits(num)
      bit_count_nums[set_bits].append(num)

    idx = 0
    for i in range(max_bit_len - 1, -1, -1):
      for num in bit_count_nums[i]:
        array[idx] = num
        idx += 1

    return array

  def bit_len(self, num):
    count = 0
    while num:
      count += 1
      num >>= 1

    return count

  def count_set_bits(self, num):
    count = 0
    while num:
      if num & 1 == 1: count += 1
      num >>= 1

    return count

test_class(Solution3, examples)

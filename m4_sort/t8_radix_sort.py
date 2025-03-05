from utils import test_class

examples = [
  {
    'input': [[10, 21, 17, 34, 44, 1236, 11, 654]],
    'output': [10, 11, 17, 21, 34, 44, 654, 1236]
  }
]

# Linear sorting algorithm that processes elements digit by digit
# Distributes elements into buckets based on each digit's value
# Time Complexity: O(d * (n + b))
  # Where d is the number of digits, b is the base of the number system used
  # If k is the max element, d = logb(k)
# Auxiliary Space: O(n + b)
class RadixSort:
  def digit_at(self, item, digit_position):
    return (item // (10 ** digit_position)) % 10

  def count_sort(self, array, digit_position):
    length = len(array)
    digit_count = 10
    item_positions = [0] * digit_count
    sorted_array = [0] * length

    for item in array:
      digit = self.digit_at(item, digit_position)
      item_positions[digit] += 1

    for digit in range(digit_count - 1):
      item_positions[digit + 1] += item_positions[digit]

    for item in reversed(array):
      digit = self.digit_at(item, digit_position)
      position = item_positions[digit]
      sorted_array[position - 1] = item
      item_positions[digit] -= 1

    for index in range(length):
      array[index] = sorted_array[index]

  def solve(self, array):
    max_item = max(array)
    max_digits = len(str(max_item))

    for digit_position in range(max_digits):
      self.count_sort(array, digit_position)
      print(digit_position, array)

    return array

test_class(RadixSort, examples)

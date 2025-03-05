from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Non-comparision based sort that works well if there limited range of values
# Counts frequency of elements and places them in their correct position\
# Stable sort, but doesn't work on decimal values
# Time Complexity: O(n + k), where k is the largest element
  # Best, Worst, Average: O(n + k)
# Auxiliary Space: O(k)
class CountSort:
  def solve(self, array):
    max_item = max(array)
    item_counts = [0] * (max_item + 1)

    for item in array:
      item_counts[item] += 1

    index = 0
    for item in range(max_item + 1):
      count = item_counts[item]

      for _ in range(count):
        array[index] = item
        index += 1

    return array

# Time Complexity: O(n + k), where k is the largest element
  # Best, Worst, Average: O(n + k)
# Auxiliary Space: O(n + k)
class PositionalCountSort:
  def solve(self, array):
    length = len(array)
    max_item = max(array)
    item_positions = [0] * (max_item + 1)
    sorted_array = [0] * (length)

    # Calculate the count of elements
    for item in array:
      item_positions[item] += 1

    # Calculate the position of elements by cumulating counts
    for item in range(max_item):
      item_positions[item + 1] += item_positions[item]

    # Iterating from the last keeps the original order, that's why it is a stable sort
    # This is because highest position is assigned to the higher element in the original order
    # This is not prominent for integers, but important in case of other data types
    # like pairs, objects with additional info, radix sort
    for item in array:
      position = item_positions[item]
      sorted_array[position - 1] = item
      item_positions[item] -= 1

    for index in range(length):
      array[index] = sorted_array[index]

    return array

test_class(CountSort, examples)
test_class(PositionalCountSort, examples)

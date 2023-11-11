from utils import test

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

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

class PositionalCountSort:
  def solve(self, array):
    length = len(array)
    max_item = max(array)
    item_positions = [0] * (max_item + 1)
    sorted_array = [0] * (length)

    for item in array:
      item_positions[item] += 1

    for item in range(max_item):
      item_positions[item + 1] += item_positions[item]

    # Iterating from the last keeps the original order. That's why it is a stable sort.
    # This is because highest position is assigned to the higher element in the original order.
    # This is not prominent for integers, but important in case of sorting:
    # pairs, objects with additional info, radix sort
    for item in array:
      position = item_positions[item]
      sorted_array[position - 1] = item
      item_positions[item] -= 1

    for index in range(length):
      array[index] = sorted_array[index]

    return array

test(CountSort, examples)
test(PositionalCountSort, examples)

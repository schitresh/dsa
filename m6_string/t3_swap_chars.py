from utils import test_class

# Traverse a string from the beginning. Swap a char with the char after k places from it.
# Repeat this process for the given number of times.

examples = [
  {
    'input': ['abcdefgh', 4, 3], # [string, times, k_places]
    'output': 'defgbcah'
  },
  {
    'input': ['abcde', 10, 6],
    'output': 'adebc'
  }
]

# Time Complexity: O(times)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string, times, places):
    places = places % len(string)
    string = list(string)

    for i in range(times):
      index = i % len(string)
      swap_index = (index + places) % len(string)
      string[index], string[swap_index] = string[swap_index], string[index]

    return ''.join(string)

test_class(Solution, examples)

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string, times, places):
    places = places % len(string)
    frequency = times // len(string)
    remaining_times = times % len(string)

    rotate_part1_by = ((len(string) % places) * frequency) % places
    rotate_part2_by = (places * frequency) % (len(string) - places)

    part1 = self.rotate_left(string[0 : places], rotate_part1_by)
    part2 = self.rotate_left(string[places : ], rotate_part2_by)
    string = list(part1 + part2)

    for i in range(remaining_times):
      index = i % len(string)
      swap_index = (index + places) % len(string)
      string[index], string[swap_index] = string[swap_index], string[index]

    return ''.join(string)

  def rotate_left(self, string, position):
    return string[position : ] + string[0 : position]

test_class(Solution2, examples)

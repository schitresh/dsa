from utils import test

# For a given string, swap char with given places after it.
# Repeat this for given number of times advancing one position at a time.
examples = [
  {
    'input': ['abcdefgh', 4, 3],
    'output': 'defgbcah'
  },
  {
    'input': ['abcde', 10, 6],
    'output': 'adebc'
  }
]

# Time Complexity: O(swap_till)
# Space Complexity: O(1)
# Brute Force
class Solution:
  def solve(self, string, times, places):
    places = places % len(string)
    string = list(string)

    for i in range(times):
      index = i % len(string)
      swap_index = (index + places) % len(string)
      string[index], string[swap_index] = string[swap_index], string[index]

    return ''.join(string)

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def rotate_left(self, string, position):
    return string[position : ] + string[0 : position]

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

test(Solution, examples)
test(Solution2, examples)

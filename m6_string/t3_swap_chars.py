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

# Naive Approach
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

# Observing Pattern
# Observe the string formed after every N successive iterations and swaps (let’s call it
# one full iteration). We get a pattern with two parts, each rotated by some places.
# The first part is rotated right by (N % C) places every full iteration. The second part
# is rotated left by C places every full iteration. We can calculate the number of full
# iterations f by dividing Times by N.
# So, the first part will be rotated left by (N % C) * f . This value can go beyond C,
# so it is effectively ((N % C) * f) % C.
# The second part will be rotated left by C * f places. This value can go beyond the
# length of the second part (N – C), so it is effectively ((C * f) % (N – C)).
# After f full iterations, there may still be some iterations remaining to complete. This
# value is Times % N which is less than N. We can follow the naive approach on these
# remaining iterations after f full iterations to get the resultant string.
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

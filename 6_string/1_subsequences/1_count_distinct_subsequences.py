from utils import test_class

examples = [
  {
    'input': ['abcd'],
    'output': 15
  }
]

ASCII_COUNT = 256

# Time Complexity: O(2^n)
# Auxiliary Space: O(n) due to recursive stack
class Solution:
  def __init__(self):
    self.count = 0

  def generate_subsequences(self, string, prefix, index):
    if index == len(string):
      if len(prefix) > 0:
        self.count += 1
      return

    # Include the current char
    self.generate_subsequences(string, prefix + string[index], index + 1)
    # Exclude the current char
    self.generate_subsequences(string, prefix, index + 1)

  def solve(self, string):
    self.generate_subsequences(string, '', 0)
    return self.count

# Dynamic Programming
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string):
    # Last index where a char occurred
    char_last_index = [-1] * (ASCII_COUNT + 1)
    # Count of distinct subsequences till length denoted by index
    # There will be only one subsequence with length 0, i.e. empty string
    # Start with length 0 because further subsequences will append chars to it
    length_count = [1]

    for i in range(len(string)):
      length = i + 1
      char_num = ord(string[i])
      last_index = char_last_index[char_num]
      char_last_index[char_num] = i

      # For each of the last subsequences,
      # we can either include or exclude the current char
      # So for current iteration, count will be 2 * count of last subsequences
      count = 2 * length_count[length - 1]
      length_count.append(count)

      if last_index != -1:
        # Assume that the char is 'b'
        # Last occurrence:
        # When the char occurred last time, it was appended to the previous subsequences
        # Previous subsequences: '', 'a'
        # Iteration subsequences: '', 'a', 'b', 'ab'
        # Length for these previous subsequences = last_length - 1 = last_index
        # Current occurrence:
        # All those subsequences are carry forwarded here
        # And we are appending the char again to those subsequences creating duplicates
        # Previous subsequences: '', 'a', 'b', 'ab', ....
        # Iteration subsequences: '', 'a', 'b', 'ab', ...., 'b', 'ab', 'bb', 'abb', ....
        length_count[length] -= length_count[last_index]

    # Subtract count of empty subsequence
    return length_count[len(string)] - 1


# Time Complexity: O(n)
# Auxiliary Space: O(n)
# Improvement over DP solution: Store the count directly instead of tracking indexes
class Solution3:
  def solve(self, string):
    if len(string) == 0:
      return 0

    # Count of previous subsequences to last occurrence for each char
    # Instead of storing last index in DP solution, this stores the count directly
    char_last_prev_count = [-1] * (ASCII_COUNT + 1)
    # Start with length 0, it will have one subsequence, i.e. empty string
    # Further subsequences will append char to it
    count = 1

    for i in range(len(string)):
      char_num = ord(string[i])
      last_prev_count = char_last_prev_count[char_num]
      char_last_prev_count[char_num] = count

      count = 2 * count

      if last_prev_count > 0:
        # As explained in DP solution
        count -= last_prev_count

    return count - 1

test_class(Solution, examples)
test_class(Solution2, examples)
test_class(Solution3, examples)

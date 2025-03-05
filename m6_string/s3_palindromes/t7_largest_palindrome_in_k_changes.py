from utils import test_class

# Given a string containing all digits, convert it into a palindrome
# by changing at most k digits
# If there are multiple solutions, then return the lexicographically largest

examples = [
  {
    'input': ['43435', 3],
    'output': '93939'
  },
  {
    'input': ['43435', 1],
    'output': '53435'
  },
  {
    'input': ['12345', 1],
    'output': '' # Not possible
  }
]

# Recursion, similar to matrix chain multiplication
# Try making cuts at all possible places and calculate the min cost
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string, count):
    pal = list(string)

    left = 0
    right = len(string) - 1

    while left < right:
      if string[left] != string[right]:
        pal[left] = pal[right] = max(string[left], string[right])
        count -= 1

      if count < 0:
        return ''

      left += 1
      right -= 1

    left = 0
    right = len(string) - 1

    while left < right:
      if pal[left] < '9':
        changed = pal[left] != string[left] or pal[right] != string[right]

        if count >= 2 and not changed:
          pal[left] = pal[right] = '9'
          count -= 2
        elif count >= 1 and changed:
          pal[left] = pal[right] = '9'
          count -= 1

      left += 1
      right -= 1

    # After the loop, left must be equal to right
    # And if there is any count left, maximize it to '9'
    if count > 0:
      pal[left] = '9'

    return ''.join(pal)

test_class(Solution, examples)

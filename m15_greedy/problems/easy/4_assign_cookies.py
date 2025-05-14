from utils import test_class

# Given two arrays greed[] and cookie[], such that greed[i] denotes the minimum cookie
# size wanted by ith child and cookie[i] denotes the size of ith cookie. Find the maximum
# number of children that can be satisfied by assigning them cookies, with each child
# getting at most 1 cookie.
# Note: A child will be satisfied if he is assigned a cookie of size at least equal to his
# greed. In other words, the ith child will be satified with jth cookie only if
# greed[i] <= cookie[j].

examples = [
  {
    'input': [[1, 2, 3], [1, 1]], # greeds, cookies
    'output': 1, # Can only assign the first or second cookie to the first child
  },
  {
    'input': [[1, 2], [1, 2, 3]],
    'output': 2, # Assign first cookie to first child & second cookie to second child
  }
]

# Time Complexity: O(n * log(n) + m * log(m))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, greeds, cookies):
    greeds.sort()
    cookies.sort()

    greed_index = len(greeds) - 1
    cookie_index = len(cookies) - 1
    count = 0

    while greed_index >= 0 and cookie_index >= 0:
      if greeds[greed_index] <= cookies[cookie_index]:
        count += 1
        greed_index -= 1
        cookie_index -= 1
      else:
        greed_index -= 1

    return count

test_class(Solution, examples)

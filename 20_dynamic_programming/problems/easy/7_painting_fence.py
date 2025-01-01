from utils import test_class

# Given a fence with n posts and k colors, find the number of ways of painting the fence
# so that not more than two consecutive posts have the same color.

examples = [
  {
    'input': [2, 4], # posts, colors
    'output': 16,
  },
  {
    'input': [3, 2],
    'output': 6,
  },
  {
    'input': [3, 4],
    'output': 60,
  },
  {
    'input': [4, 3],
    'output': 66,
  },
]

# Recursion
# Case 1: Different color previous post
# If we paint the current post a different color from the one before it, we have k - 1
# choices (all colors except the previous post’s color). This means the number of ways to
# paint the first n-1 posts is multiplied by k-1.
# Case 2: Same color for the last two posts
# If the last two posts are the same color, they must differ from the post before them
# (the third-last post). Thus, we have k-1 choices for the last two posts, and the number
# of ways to paint the first n-2 posts is given by ways(n-2).
# So, ways(n) = ways(n - 1) * (k - 1) + ways(n - 2) * (k - 1)
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, posts, colors):
    return self.paint(posts, colors)

  def paint(self, posts, colors):
    if posts == 1: return colors
    if posts == 2: return colors * colors

    count1 = self.paint(posts - 1, colors) * (colors - 1)
    count2 = self.paint(posts - 2, colors) * (colors - 1)

    return count1 + count2

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, posts, colors):
    self.memo = [None] * (posts + 1)
    return self.paint(posts, colors)

  def paint(self, post, colors):
    if post == 1: return colors
    if post == 2: return colors * colors

    if self.memo[post]:
      return self.memo[post]

    count1 = self.paint(post - 1, colors) * (colors - 1)
    count2 = self.paint(post - 2, colors) * (colors - 1)

    self.memo[post] = count1 + count2
    return self.memo[post]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, posts, colors):
    dp = [None] * posts
    dp[0] = colors
    dp[1] = colors * colors

    for post in range(2, posts):
      dp[post] = dp[post - 1] * (colors - 1)
      dp[post] += dp[post - 2] * (colors - 1)

    return dp[-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, posts, colors):
    prev2 = colors
    prev1 = colors * colors

    for _ in range(2, posts):
      curr = prev1 * (colors - 1)
      curr += prev2 * (colors - 1)

      prev2 = prev1
      prev1 = curr

    return prev1

test_class(Solution4, examples)

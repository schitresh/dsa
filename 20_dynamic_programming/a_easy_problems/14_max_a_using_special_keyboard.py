from utils import test_class

# Imagine you have a special keyboard with the following keys:
# Key 1: Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it
#                  after what has already been printed.
# If you can only press the keyboard for N times (with the above four keys),
# write a program to produce maximum numbers of A's. That is to say,
# the input parameter is N (No. of keys that you can press), the output is M
# (No. of As that you can produce).

examples = [
  {
    'input': [3],
    'output': 3, # A, A, A
  },
  {
    'input': [7],
    'output': 9, # A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
  },
  {
    'input': [11],
    'output': 27,
    # A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
  },
]

# Recursion
# Time Complexity: O(3^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, presses):
    return self.max_a(presses, 0, 0)

  def max_a(self, presses, a_count, copy_count):
    if presses <= 0: return a_count

    # Press key1 to print A
    count1 = self.max_a(presses - 1, a_count + 1, 0)
    # Press key2 & key3 to select all & copy
    # These two keys need to be pressed one after the other to achieve that
    count2 = self.max_a(presses - 2, a_count, a_count)
    # Press key3 to paste the copied As
    count3 = self.max_a(presses - 1, a_count + copy_count, copy_count)

    return max(count1, count2, count3)

test_class(Solution, examples)

# Recursion
# 1. For N <= 6, the output is N itself
# 2. Ctrl-V can be used multiple times to print current buffer. The sequence of N
# keystrokes which produces an optimal string length will end with a suffix of
# Ctrl-A, Ctrl-C, followed by only Ctrl-V’s. This is for N > 6.
# The task is to find the breakpoint after which we get the above suffix of keystrokes.
# Since these keystrokes require a minimum of 3 keys (Ctrl-A, Ctrl-C, Ctrl-V),
# we can loop from N - 3 to 1 and choose each of these values for the breakpoint,
# computing the optimal string they would produce. Once the loop ends, we will have
# the maximum of the optimal lengths for various breakpoints, thereby giving us the
# optimal length for N keystrokes.
# Time Complexity: O(n!)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, presses):
    return self.max_a(presses)

  def max_a(self, presses):
    if presses <= 6: return presses

    count = 0

    for brkpoint in range(presses - 3, 0, -1):
      max_before_brkpoint = self.max_a(brkpoint)
      presses_after_brkpoint = presses - brkpoint - 1
      curr = presses_after_brkpoint * max_before_brkpoint
      count = max(count, curr)

    return count

test_class(Solution2, examples)

# Memoization
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, presses):
    self.memo = [None] * (presses + 1)
    return self.max_a(presses)

  def max_a(self, presses):
    if presses <= 6: return presses

    if self.memo[presses]:
      return self.memo[presses]

    count = 0

    for brkpoint in range(presses - 3, 0, -1):
      max_before_brkpoint = self.max_a(brkpoint)
      presses_after_brkpoint = presses - brkpoint - 1
      curr = presses_after_brkpoint * max_before_brkpoint
      count = max(count, curr)

    self.memo[presses] = count
    return count

test_class(Solution3, examples)

# Tabulation
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, presses):
    if presses <= 6: return presses
    dp = [0] * (presses + 1)

    for i in range(7):
      dp[i] = i

    for i in range(7, presses + 1):
      for j in range(presses - 3, 0, -1):
        curr = (i - j - 1) * dp[j]
        dp[i] = max(dp[i], curr)

    return dp[-1]

test_class(Solution4, examples)

# Tabulation with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution5:
  def solve(self, presses):
    if presses <= 6: return presses
    dp = [0] * (presses + 1)

    for i in range(7):
      dp[i] = i

    for i in range(7, presses + 1):
      # For any keystroke i, we will need to choose between:
      # 1. Press Ctrl-V once after copying the A's obtained by n - 3 keystrokes
      # 2. Press Ctrl-V twice after copying the A's obtained by n - 4 keystrokes
      # 3. Press Ctrl-V thrice after copying the A's obtained by n - 5 keystrokes
      dp[i] = max(2 * dp[i - 3], 3 * dp[i - 4], 4 * dp[i - 5])

    return dp[-1]

test_class(Solution5, examples)

## Dynamic Programming
- Breaks down a complex problem into simpler subproblems that are interdependent
- Avoids redundant computations by solving each subproblem only once
  - And storing the results
  - Which builds up the solution to the main problem
- Used when problem consists of
  - Optimal substructure
    - Optimal results of subproblems can be combined
    - To achieve the optimal result of the bigger problem
    - Example: Finding minimum cost path in a weighted graph
      - Find minimum cost path from source to each intermediate node
      - Find minimum cost path from each intermediate to destination node
  - Overlapping subproblem
    - The same subproblems are solved repeatedly in different parts of the problem
    - Example: Computing fibonacci series
      - f(n) = f(n - 1) + f(n - 2) and f(n - 1) = f(n - 2) + f(n - 3)
      - Hence, f(n - 2) is computed twice

## Approaches to DP
- Top-Down (Memoization)
  - Starts with the final solution
    - And recursively breaks it down into smaller subproblems
  - Suitable when the number of subproblems is large and many of them are reused
    - State transition is relatively difficult to think
    - Slow due to a lot of recursive calls and return statements
  - Generally a recursive approach
    - Entries are filled on demand and all entries are not necessarily filled
- Bottom-Up (Tabulation)
  - Starts with the smallest subproblem
    - And gradually builds up to the final solution
  - Suitable when the number of subproblems is small
    - State transition is relatively easy to think
    - Faster since previous states are directly accessed from the table
  - Generally an iterative approach
    - Starting from the first entry, all entries are filled one by one

## Fibonnaci
```py
# Naive Approach
# Time Complexity: O(2^n)
# Auxiliary Space: O(n) for recursive stack
class Fib:
  def solve(self, n):
    if n <= 1: return n

    x = fib(n - 1)
    y = fib(n - 2)
    return x + y

# Top-Down (Memoization)
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Fib:
  def __init__(self):
    self.fib_series = []

  def solve(self, n):
    self.fib_series = [None] * (n + 1)
    self.fib(n)

  def fib(self, n):
    if n <= 1: return n

    if self.fib_series[n]:
      return self.fib_series[n]

    x = self.fib(n - 1)
    y = self.fib(n - 2)
    self.fib_series[n] = x + y

    return self.fib_series[n]

# Bottom-Up (Tabulation)
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Fib:
  def solve(self, n):
    fib_series = [None] * (n + 1)
    fib_series[0] = 0
    fib_series[1] = 1

    for i in range(2, n + 1):
      fib_series[i] = fib_series[i - 1] + fib_series[i - 2]

    return fib_series[n]

# Bottom-Up (Tabulation) with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Fib:
  def solve(self, n):
    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
      fib3 = fib2 + fib1
      fib1 = fib2
      fib2 = fib3

    return fib3
```

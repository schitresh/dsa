## Dynamic Programming
- Breaks down a complex problem into simpler subproblems that are interdependent
- Optimization over plain recursion by storing results of subproblems
- Avoids redundant computations by solving each subproblem only once
  - And storing the results
  - Which builds up the solution to the main problem

## Properties
- DP is used when problem consists of optimal substructure or overlapping subproblems

### Optimal substructure
- Optimal results of subproblems can be combined
- To achieve the optimal result of the bigger problem
- Example: Finding minimum cost path in a weighted graph
  - Find minimum cost path from source to each intermediate node
  - Find minimum cost path from each intermediate to destination node

### Overlapping subproblems
- The same subproblems are solved repeatedly in different parts of the problem
- Example: Computing fibonacci series
  - f(n) = f(n - 1) + f(n - 2) and f(n - 1) = f(n - 2) + f(n - 3)
  - Hence, f(n - 2) is computed twice

## Approaches to DP
### Top-Down (Memoization)
- Starts with the final solution
  - And recursively breaks it down into smaller subproblems
- Suitable when the number of subproblems is large and many of them are reused
  - State transition is relatively difficult to think
  - Slow due to a lot of recursive calls and return statements
- Generally a recursive approach
  - Entries are filled on demand and all entries are not necessarily filled

### Bottom-Up (Tabulation)
  - Starts with the smallest subproblem
    - And gradually builds up to the final solution
  - Suitable when the number of subproblems is small
    - State transition is relatively easy to think
    - Faster since previous states are directly accessed from the table
  - Generally an iterative approach
    - Starting from the first entry, all entries are filled one by one

## Steps to Solve
- Identify if it is a dynamic programming problem
  - Typically, DP problems require
    - maximizing or minimizing certain quantities
    - or counting problems that say to count the arrangements under certain conditions
    - or certain probability problems
  - DP problems satisfy the overlapping subproblems property
    - and most of the classic DP problems also satisfy the optimal substructure property
- Decide a state expression with the least parameters
  - DP problems are all about the state and its transition
    - This is the most basic step which must be done very carefully
    - Because the state transition depends on the choice of state definition you make
  - A state can be defined as the set of parameters
    - That can uniquely identify a certain position or standing in the given problem
    - This set of parameters should be as small as possible to reduce state space
  - In the famous Knapsack problem, state is defined by two parameters index and weight
    - The parameters index and weight together can uniquely identify a subproblem
    - DP[index][weight] tells the maximum profit it can make
      - by taking items from range 0 to index having the capacity of sack to be weight
- Formulate state and transition relationship
  - This is the hardest part and requires a lot of intuition, observation, and practice
- Adding memoization or tabulation for the state
  - Store the state answer so that the next time that state is required
    - it can be directly used from the memory


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

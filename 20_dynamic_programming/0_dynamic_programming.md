## Dynamic Programming
- Breaks down a complex problem into simpler subproblems that are interdependent
- Optimization over plain recursion by storing results of subproblems
- Avoids redundant computations
  - By solving each subproblem only once and storing the results
  - Which builds up the solution to the main problem

## Properties
- DP is used when problem consists of optimal substructure and overlapping subproblems

### Optimal substructure
- Optimal results of subproblems can be combined
  - To achieve the optimal result of the bigger problem
- Example: finding minimum cost path in a weighted graph
  - Find minimum cost path from source to each intermediate node
  - Find minimum cost path from each intermediate to destination node
  - Combining them can achieve the minimum cost path

### Overlapping subproblems
- The same subproblems are solved repeatedly in different parts of the problem
- Example: Computing fibonacci series
  - f(n) = f(n - 1) + f(n - 2)
  - f(n - 1) = f(n - 2) + f(n - 3)
  - Hence, f(n - 2) is being computed twice here

## Approaches to DP
### Memoization (Top-Down)
- Starts with the final solution
  - And recursively breaks it down into smaller subproblems
- Suitable when the number of subproblems is large and many of them are reused
  - State transition is relatively difficult to think
  - Slow due to a lot of recursive calls and return statements
- Generally a recursive approach
  - Entries are filled on demand and all entries are not necessarily filled

### Tabulation (Bottom-Up)
- Starts with the smallest subproblem
  - And gradually builds up to the final solution
- Suitable when the number of subproblems is small
  - State transition is relatively easy to think
  - Faster since previous states are directly accessed from the table
- Generally an iterative approach
  - Starting from the first entry, all entries are filled one by one

## Steps to Solve
### Identify if it is DP problem
- Typically, DP problems require one of the following
  - Maximizing or minimizing certain quantities
  - Counting some arrangements under certain conditions
  - Certain probability problems
- DP problems satisfy the overlapping subproblems property
- Most of the classic DP problems also satisfy the optimal substructure property

### Decide a state expression with minimum parameters
- DP problems are all about the state and its transition
  - This is the most basic step which must be done very carefully
  - Because the state transition depends on the choice of state definition you make
- A state can be defined as a set of parameters
  - That can uniquely identify a certain position or standing in the given problem
  - This set of parameters should be as small as possible to reduce state space
- In the famous Knapsack problem, state is defined by two parameters: index and weight
  - The parameters index and weight together can uniquely identify a subproblem
  - dp[index][weight] tells the maximum profit it can make
    - By taking items from range 0 to index within the capacity of the sack

### Formulate state and transition relationship
- How the state will transition at each step of recursion or iteration
- This is the hardest part and requires a lot of intuition, observation, and practice

### Adding memoization or tabulation for the state
- Store the state answer
- The next time that state is required, it can be directly used from the memory

## Example: Fibonnaci
```py
# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Fib:
  def solve(self, n):
    if n <= 1: return n

    x = fib(n - 1)
    y = fib(n - 2)
    return x + y

# Memoization (Top-Down)
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Fib:
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

# Tabulation (Bottom-Up)
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Fib:
  def solve(self, n):
    fib_series = [None] * (n + 1)
    # Base cases
    fib_series[0] = 0
    fib_series[1] = 1

    for i in range(2, n + 1):
      fib_series[i] = fib_series[i - 1] + fib_series[i - 2]

    return fib_series[n]

# Tabulation (Bottom-Up) with space optimization
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

    return fib2
```

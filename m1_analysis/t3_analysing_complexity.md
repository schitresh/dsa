## Common Runtimes
- Specified in order of increasing complexity
- Constant: O(1)
  - Does not depend on the size of the input
  - If there is no loop, no recursion, no call to non-constant time function
  - Though a loop or recursion that runs a constant number of times is also considered O(1)
- Logarithmic: O(log(n))
  - If the loop variables are divided or multiplied by a constant amount
  - Also for recursive calls in a recursive function
- Linear: O(n)
  - Run time is proportional to the size of the input
  - If the loop variables are incremented or decremented by a constant amount
- Linear Logarithmic: O(n * log(n))
  - For example, merge sort
- Quadratic: O(n^2)
  - For an input size of n, the algo takes n * n steps to complete the operation
  - For example, a linear loop nested within a linear loop
- Polynomial: O(n^k)
- Exponential: O(2^n)
  - Running time doubles with each addition to the input data set
  - For example, generating all subsets of a set
- Factorial: O(n!)

## General Outline
- Substitute the input size into the recurrence relation to obtain a sequence of terms
- Identify a pattern in the sequence of terms to obtain a closed-form expression
- Determine the order of growth of the closed-form expression
  - By using techniques like master theorem
  - Or by finding the dominant term and ignoring lower order terms
- Use the order of growth to determine the asymptotic upper bound

## Substitution Method
- Make a guess for the solution
- And then use mathematical induction to prove the guess is correct or incorrect

## Recurrence Tree Method
- Draw a recurrence tree and calculate the time taken by every level of the tree
- Start from the given recurrence and keep drawing till we find a pattern among levels
- To get an upper bound, sum the infinite series

## Master Method
- Works for the recurrences that are or can be transformed into this form
  - T(n) = a * T(n/b) + f(n), where a >= 1 and b > 1
- There are three cases
  - If f(n) = O(n^c) and c < logb(a), then T(n) = Θ(n^logb(a))
  - If f(n) = Θ(n^c) and c = logb(a), then T(n) = Θ(n^logb(a) * log(n))
  - If f(n) = Ω(n^c) and c > logb(a), then T(n) = Θ(f(n))
- Mainly derived from the recurrence tree method
  - If we draw the recurrence tree of T(n) = a * T(n/b) + f(n)
    - The height of the tree is logb(n)
  - We can see that the work done at the root is f(n)
    - And the work done at all the leaves is n^logb(a)
  - If the work done at leaves is polynomially more
    - Then leaves are the dominant part
  - If the work done at leaves & root is asymptotically the same
    - The result is height multiplied by work done at any level
  - If the work done at root is asymptotically more
    - Then the root is the dominant part

## Amortized Analysis
- Used for algorithms where an occasional operation is very slow
  - But most of the other operations are faster
- The idea is to spread the cost of these operations over multiple operations
  - So that the average cost of each operation is constant or less

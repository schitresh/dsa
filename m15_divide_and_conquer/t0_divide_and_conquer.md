## Divide And Conquer
- Breaks down a complex problem into smaller non-overlapping subproblems
  - Solves them individually
  - And combines the solutions to find the overall solution
- Subproblems should be non-overlapping
  - Each subproblem should be independent of the others
  - Solving one subproblem does not depend on the solution of another
  - Allows parallel processing or concurrent execution of subproblems
  - If the subproblems are overlapping, then dynamic programming is used
- Considerations
  - If the problem is simple, the overhead of dividing & merging can be an overhead
  - For large data sets
    - Need to consider the memory requirements for storing intermediate results
- Applications: Binary search, merge sort, quick sort

## Comparisons
### Decrease And Conquer
- It also simplifies complex problems by partitioning them into smaller instances
- But contrary to divide and conquer, which takles multiple subproblems
  - Decrease and conquer concentrates on resolving a single subproblem
- For example
  - Merge sort & quick sort are divide & conquer because there are two subproblems
  - Binary search & insertion sort are decrease & conquer because there is one subproblem

### Dynamic Programming
- Similar to divide and conquer but subproblems are interdependent
- Results of subproblems are stored and used for future references
  - For similar or overlapping subproblems

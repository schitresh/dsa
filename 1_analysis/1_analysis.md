## Analysis
- Performance
  - How much time & memory is used when a program is run
  - Depends on how the code is written, machine, compiler, etc.
- Complexity
  - How do the resource requirement of a program or algorithm scale
  - What happens as the size of the problem being solved gets larger
  - Complexity affects performance but not vice-versa

## Algorithm Analysis
- Provides theoretical estimation for the required resources of a algorithm
- Determines the amount of time and space required to execute it
- Useful way to measure the efficiency rather than implementating the algorithm directly
- Types
  - Best case: Input for which the algo takes the minimum time
  - Worst case: Input for which the algo takes the maximum time
  - Average case: Average of computation time of all the random inputs

## Asymptotic Analysis
- Evaluates the performance of an algorithm in terms of input size
  - Without actually measuring the running time
  - Calculates how time/space taken by the algo increase with the input size
- For example
  - Consider running linear search on fast computer & binary search on slow computer
  - For small values of input size
    - The fast computer with linear search may take less time
  - But after a certain value of input size
    - The slow computer with binary search will definitely take less time
- If two algorithms are asymptotically the same
  - We cannot judge which one is better since constants are ignored in asymptotic analysis
- It might be possible that the large input values (larger than the constant)
  - Are never given to your software
  - And an asymptotically slower algorithm performs better for your particular situation
  - So you may end up choosing that algorithm for your use case

## Asymptotic Notations
- f(n) = Actual function
- g(n) = Bounding function
  - g(n) will always return positive values since the time taken cannot be negative
- n0 = The largest value of n from where the boundation is valid for all further values
  - Hence the notations are valid for n >= n0
- c = Positive constant (c > 0)

## Big O Notation
- Provides an upper bound on the growth rate
- Represents the worst case scenario
- O(n) means that the running time increases linearly with the input size of n or less

```math
O(g(n)) = { f(n): f(n) <= c * g(n) }
```

## Big Omega Notation
- Provides a lower bound on the growth rate
- Represents the best case scenario
- Ω(n) means that the running time increases linearly with the input size of n or more

```math
Ω(g(n)) = { f(n): f(n) >= c * g(n) }
```

## Big Theta Notation
- Provides both an upper bound and lower bound on the growth rate
  - Bounded by O and Ω
- Represents the average case scenario
- Θ(n) means that the running time increases linearly with the input size of n

```math
Θ(g(n)) = { f(n) : c1 * g(n) <= f(n) <= c2 * g(n) }
```

## Little Notations (o, ω)
- Loosely bound
- For large n, f(n) and g(n) vary greatly

```math
o: Lim(n -> ∞) f(n)/g(n) = 0
```

```math
ω: Lim(n -> ∞) f(n)/g(n) = ∞
```

## Properties
- For a constant 'a'
  - If f(n) is O(g(n)), then a * f(n) is also O(g(n))
- Transitive
  - If f(n) is O(g(n)) and g(n) is O(h(n)), then f(n) = O(h(n))
- Reflexive
  - If f(n) is given, then f(n) is O(f(n))
  - Since maximum value of f(n) will be f(n) itself
  - Hence x = f(n) and y = O(f(n)) tie themselves in reflexive relation always
- Symmetric
  - This property only satisfies for Θ notation
  - If f(n) is Θ(g(n)), then g(n) is Θ(f(n))
- Transpose Symmetric
  - This property only satisfies O and Ω notations
  - If f(n) is O(g(n)), then g(n) is Ω (f(n))

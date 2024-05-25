- f(n) = Actual function
- g(n) = Bounding function

- n0 = The largest value of n from where the boundation is valid for all further values
- c = Positive constant (c > 0)

## Big O Notation
- Upper bound
- Worst case

```math
O(g(n)) = { f(n): f(n) <= c * g(n) }
```

## Big Omega Notation
- Lower bound
- Best case

```math
Ω(g(n)) = { f(n): c * g(n) <= f(n) }
```

## Big Theta Notation
- Average case
- Bounded by O and Ω

```math
Θ(g(n)) = { f(n) : c1 * g(n) <= f(n) <= c2 * g(n) }

g(n) = O(n) && g(n) = Ω(n)
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

# Pow(x, n)

## Problem Description
Implement `pow(x, n)`, which calculates `x` raised to the power `n`.

## Approach
Fast exponentiation (binary exponentiation). If n is negative, invert x and negate n. Then iteratively: if the current bit of n is set, multiply the result by x. Square x and right-shift n each iteration.

## Complexity
- **Time:** O(log n)
- **Space:** O(1)

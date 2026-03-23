# Min Stack

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1) time.

## Approach
Store each element as a `(value, current_min)` pair. When pushing, compute the new minimum as `min(val, previous_min)`. This way the minimum at any stack depth is always stored alongside the element, so `getMin` is a simple lookup at the top of the stack.

## Complexity
- **Time:** O(1) for all operations
- **Space:** O(n)

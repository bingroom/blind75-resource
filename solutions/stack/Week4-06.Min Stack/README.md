# Min Stack

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1) time.


## Solution

```python
# LC 155. Min Stack (Medium)
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []      # stores (value, current_min) pairs

    def push(self, val: int) -> None:
        cur_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

## Approach
Store each element as a `(value, current_min)` pair. When pushing, compute the new minimum as `min(val, previous_min)`. This way the minimum at any stack depth is always stored alongside the element, so `getMin` is a simple lookup at the top of the stack.

## Complexity
- **Time:** O(1) for all operations
- **Space:** O(n)

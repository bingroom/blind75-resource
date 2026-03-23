# Implement Queue using Stacks

**Topic:** Stack

## Problem Description
Implement a first-in-first-out (FIFO) queue using only two stacks. The queue should support `push`, `pop`, `peek`, and `empty` operations.


## Solution

```python
# LC 232. Implement Queue using Stacks (Easy)
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.in_stack = []   # for push
        self.out_stack = []  # for pop/peek

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        """Transfer elements from in_stack to out_stack only when out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

## Approach
Use two stacks: an `in_stack` for pushes and an `out_stack` for pops/peeks. When `out_stack` is empty and we need to pop or peek, transfer all elements from `in_stack` to `out_stack` by popping and pushing. This reversal gives us FIFO order. The key insight is that we only transfer when `out_stack` is empty, which gives amortized O(1) per operation since each element is moved at most once.

## Complexity
- **Time:** O(1) amortized per operation
- **Space:** O(n)

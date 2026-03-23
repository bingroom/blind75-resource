# Implement Queue using Stacks

## Problem Description
Implement a first-in-first-out (FIFO) queue using only two stacks. The queue should support `push`, `pop`, `peek`, and `empty` operations.

## Approach
Use two stacks: an `in_stack` for pushes and an `out_stack` for pops/peeks. When `out_stack` is empty and we need to pop or peek, transfer all elements from `in_stack` to `out_stack` by popping and pushing. This reversal gives us FIFO order. The key insight is that we only transfer when `out_stack` is empty, which gives amortized O(1) per operation since each element is moved at most once.

## Complexity
- **Time:** O(1) amortized per operation
- **Space:** O(n)

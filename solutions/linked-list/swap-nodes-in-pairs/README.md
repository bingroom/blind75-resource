# Swap Nodes in Pairs

- **LeetCode:** [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Problem Description
Given a linked list, swap every two adjacent nodes and return its head. You must solve it without modifying the values in the nodes (i.e., only nodes themselves may be changed).

## Approach
1. Create a dummy node pointing to `head` to simplify edge cases.
2. Maintain a `prev` pointer that tracks the node before each pair.
3. For each pair (`first`, `second`):
   - Point `first.next` to whatever comes after `second`.
   - Point `second.next` to `first`.
   - Point `prev.next` to `second` (the new front of the pair).
4. Advance `prev` to `first` (now the tail of the swapped pair).
5. Continue until fewer than two nodes remain.

## Complexity
- **Time:** O(n) -- each node is visited once.
- **Space:** O(1) -- only pointer manipulation, no extra data structures.

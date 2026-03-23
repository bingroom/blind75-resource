# Reverse Nodes in k-Group

- **LeetCode:** [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem Description
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. If the number of nodes is not a multiple of `k`, the remaining nodes at the end stay in their original order. Only node links may be changed, not node values.

## Approach
1. Use a dummy node before the head and track `group_prev` (the node before each k-group).
2. For each group, first check if `k` nodes remain by walking forward `k` steps. If not, stop.
3. Reverse the `k` nodes in-place using the standard iterative reversal. Set `prev` to the node after the group so the reversed segment links forward correctly.
4. Update `group_prev.next` to point to `kth` (the new first node of the reversed group).
5. Advance `group_prev` to the old first node (now the last node of the reversed group).

## Complexity
- **Time:** O(n) -- each node is visited a constant number of times (once to check length, once to reverse).
- **Space:** O(1) -- all operations are pointer manipulation in-place.

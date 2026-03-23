# Middle of the Linked List

- **LeetCode:** [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Problem Description
Given the `head` of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.

## Approach
Use the slow/fast pointer technique:
1. Initialize both `slow` and `fast` to `head`.
2. Move `slow` one step and `fast` two steps each iteration.
3. When `fast` reaches the end (or goes past it), `slow` is at the middle.

For even-length lists, `slow` naturally lands on the second of the two middle nodes, which is what the problem requires.

## Complexity
- **Time:** O(n) -- single pass through the list.
- **Space:** O(1) -- only two pointers.

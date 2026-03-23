# Odd Even Linked List

- **LeetCode:** [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

## Problem Description
Given the `head` of a singly linked list, group all nodes with odd indices together followed by nodes with even indices, and return the reordered list. The first node is considered odd, the second node even, and so on. Solve in O(1) extra space and O(n) time.

## Approach
1. Maintain two pointers: `odd` starting at the first node, `even` starting at the second.
2. Save the head of the even list (`even_head`).
3. In each iteration, link the current odd node to the next odd node (skipping even), then link the current even node to the next even node (skipping odd).
4. After the loop, attach the even list to the end of the odd list.

## Complexity
- **Time:** O(n) -- single pass through the list.
- **Space:** O(1) -- rearranges nodes in-place with only pointer variables.

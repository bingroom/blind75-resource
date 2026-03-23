# Palindrome Linked List

- **LeetCode:** [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Problem Description
Given the `head` of a singly linked list, return `true` if it is a palindrome, or `false` otherwise.

## Approach
1. Use slow/fast pointers to find the middle of the list.
2. Reverse the second half of the list in-place.
3. Compare the first half with the reversed second half node by node.
4. If all values match, the list is a palindrome.

This avoids using O(n) extra space by modifying the list in-place rather than copying values to an array.

## Complexity
- **Time:** O(n) -- one pass to find middle, one pass to reverse, one pass to compare.
- **Space:** O(1) -- only pointer variables, no extra data structures.

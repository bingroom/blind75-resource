# Sort List

- **LeetCode:** [148. Sort List](https://leetcode.com/problems/sort-list/)

## Problem Description
Given the `head` of a linked list, return the list after sorting it in ascending order. The problem asks for O(n log n) time and ideally O(1) space (though O(log n) for the recursion stack is acceptable).

## Approach
Use top-down merge sort, which naturally fits linked lists:

1. **Find the middle:** Use slow/fast pointers. Start `fast` one step ahead so `slow` lands on the last node of the left half.
2. **Split:** Cut the list at the midpoint by setting `mid.next = None`.
3. **Recurse:** Sort both halves independently.
4. **Merge:** Merge the two sorted halves using a standard two-pointer merge with a dummy head.

Merge sort is ideal for linked lists because the merge step requires no extra array allocation -- we just relink existing nodes.

## Complexity
- **Time:** O(n log n) -- standard merge sort recurrence.
- **Space:** O(log n) -- recursion stack depth. The merge itself is O(1) since we reuse existing nodes.

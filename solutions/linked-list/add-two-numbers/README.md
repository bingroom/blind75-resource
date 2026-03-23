# Add Two Numbers

- **LeetCode:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

## Approach
1. Traverse both lists simultaneously, summing corresponding digits along with a carry.
2. Use `divmod(sum, 10)` to get the new carry and the current digit.
3. Create a new node for each digit and append it to the result list.
4. Continue until both lists are exhausted and carry is zero.

The reverse storage order is convenient -- it means we naturally process digits from least significant to most significant, just like manual addition.

## Complexity
- **Time:** O(max(m, n)) where m and n are the lengths of the two lists.
- **Space:** O(max(m, n)) for the output list.

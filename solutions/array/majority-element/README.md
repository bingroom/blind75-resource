# Majority Element

- **LeetCode:** [169. Majority Element](https://leetcode.com/problems/majority-element/)

## Problem Description

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `n / 2` times. You may assume that the majority element always exists in the array.

## Approach

Use the **Boyer-Moore Voting Algorithm**:

1. Maintain a `candidate` and a `count`, both starting at 0.
2. Iterate through the array:
   - If `count` is 0, set the current element as the new `candidate`.
   - If the current element equals `candidate`, increment `count`; otherwise decrement it.
3. The majority element always survives because it appears more than half the time -- every "cancellation" removes one majority and one minority element, so the majority element is guaranteed to be the final candidate.

## Complexity

- **Time:** O(n) -- single pass through the array.
- **Space:** O(1) -- only two variables.

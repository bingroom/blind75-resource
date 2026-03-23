# Random Pick with Weight

## Problem Description
Given an array `w` where `w[i]` is the weight of index `i`, implement `pickIndex()` which randomly picks an index proportional to its weight.

## Approach
Build a prefix sum array. To pick an index, generate a random integer in `[1, total_weight]` and binary search for the leftmost prefix sum that is >= that value. The prefix sum partitions the number line into segments proportional to the weights.

## Complexity
- **Time:** O(n) for initialization, O(log n) for `pickIndex`
- **Space:** O(n) for the prefix sum array

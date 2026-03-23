# Insert Delete GetRandom O(1)

- **LeetCode:** [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem Description

Implement the `RandomizedSet` class with `insert`, `remove`, and `getRandom` operations, each running in average O(1) time. `getRandom` should return each element with equal probability.

## Approach

Use two data structures together:

1. **A list** (`vals`) stores the elements, enabling O(1) random access by index for `getRandom`.
2. **A hash map** (`val_to_idx`) maps each value to its index in the list, enabling O(1) lookup for `insert` and `remove`.

The key trick for O(1) `remove`: swap the element to delete with the last element in the list, update the swapped element's index in the map, then pop the last element. This avoids shifting.

## Complexity

- **Time:** O(1) average per `insert`, `remove`, and `getRandom`.
- **Space:** O(n) where n is the number of elements in the set.

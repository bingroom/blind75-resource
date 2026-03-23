# K Closest Points to Origin

## Problem Description
Given an array of points on the X-Y plane and an integer k, return the k closest points to the origin (0, 0). Distance is Euclidean distance.

## Approach
Maintain a max-heap of size k (using negated distances with Python's min-heap). For each point, if the heap is smaller than k, push it in. Otherwise, if the point is closer than the farthest in the heap, replace the top.

## Complexity
- **Time:** O(n log k)
- **Space:** O(k)

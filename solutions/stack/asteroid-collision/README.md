# Asteroid Collision

## Problem Description
Given an array of integers representing asteroids in a row, where the absolute value is the size and the sign indicates direction (positive = right, negative = left), determine the state after all collisions. Same-direction asteroids never collide.

## Approach
Use a stack. For each asteroid, check if it collides with the top of the stack (current moves left and top moves right). If the top is smaller, pop it and keep checking. If equal, both explode. If the top is larger, the current asteroid is destroyed. If no collision occurs (same direction, or stack empty), push the asteroid.

## Complexity
- **Time:** O(n) -- each asteroid is pushed and popped at most once
- **Space:** O(n)

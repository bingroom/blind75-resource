# Asteroid Collision

**Topic:** Stack

## Problem Description
Given an array of integers representing asteroids in a row, where the absolute value is the size and the sign indicates direction (positive = right, negative = left), determine the state after all collisions. Same-direction asteroids never collide.


## Solution

```python
# LC 735. Asteroid Collision (Medium)
# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            alive = True
            # Collision only when stack top is moving right (+) and current moves left (-)
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()       # top asteroid explodes, keep checking
                elif stack[-1] == -ast:
                    stack.pop()       # both explode
                    alive = False
                    break
                else:
                    alive = False     # current asteroid explodes
                    break

            if alive:
                stack.append(ast)

        return stack
```

## Approach
Use a stack. For each asteroid, check if it collides with the top of the stack (current moves left and top moves right). If the top is smaller, pop it and keep checking. If equal, both explode. If the top is larger, the current asteroid is destroyed. If no collision occurs (same direction, or stack empty), push the asteroid.

## Complexity
- **Time:** O(n) -- each asteroid is pushed and popped at most once
- **Space:** O(n)

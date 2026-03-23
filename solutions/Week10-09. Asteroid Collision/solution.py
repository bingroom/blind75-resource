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

# Asteroid Collision

**Topic:** Stack
- **LeetCode 連結:** [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
- **難度:** Medium

## 題目描述

給定一個整數陣列代表小行星，正數向右移動，負數向左移動，絕對值代表大小。模擬碰撞後回傳剩餘的小行星。

## 解題思路

1. 使用堆疊模擬碰撞過程。
2. 碰撞只在堆疊頂為正、當前為負時發生。
3. 比較大小：較小的爆炸，相等則兩者皆爆，較大的存活。
4. 若當前小行星存活，推入堆疊。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) -- each asteroid is pushed and popped at most once
- **空間複雜度:** O(n)

# Course Schedule

- **LeetCode:** [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

 

**Example 1:**

```

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

```

**Example 2:**

```

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

```

 

**Constraints:**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= 5000`

	- `prerequisites[i].length == 2`

	- `0 <= a_i, b_i < numCourses`

	- All the pairs prerequisites[i] are **unique**.

## Solution

```python
# LeetCode 207. Course Schedule
# 時間複雜度: O(V + E)  空間複雜度: O(V)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        選修課有先修關係，判斷能否全部修完（即圖是否有環）。拓撲排序或 DFS 偵環。
        """
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        state = [0] * numCourses  # 0=未訪 1=訪問中 2=已完成

        def has_cycle(u: int) -> bool:
            state[u] = 1
            for v in adj[u]:
                if state[v] == 1:
                    return True
                if state[v] == 0 and has_cycle(v):
                    return True
            state[u] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0 and has_cycle(i):
                return False
        return True

```

## 思路

- **有向圖是否有環：** 建圖後用 DFS + 三色（未訪/訪問中/完成）偵環。若存在反向邊（到「訪問中」的節點）則有環，無法全部修完。

## 時間 / 空間複雜度

- **時間:** O(V+E)。
- **空間:** O(V)。

## 相關閱讀

- **演算法:** Topological Sort、Cycle Detection、DFS

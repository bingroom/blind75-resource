# Course Schedule

**Topic:** Graph
- **LeetCode 連結:** [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- **難度:** Medium

## 題目描述

共有 `numCourses` 門課程，以 `prerequisites` 表示先修關係：`[a, b]` 代表修課 `a` 之前必須先修課 `b`。判斷是否能完成所有課程（即先修關係中是否存在環）。

## 解題思路

1. 根據先修關係建立有向圖的鄰接表。
2. 使用 DFS 偵測環：每個節點有三種狀態——未訪問、訪問中、已完成。
3. 對每個未訪問的節點啟動 DFS；若遍歷到「訪問中」的節點，表示存在環，回傳 `False`。
4. DFS 完成後將節點標記為「已完成」。若所有節點都能完成 DFS 而無環，回傳 `True`。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(V+E)。
- **空間複雜度:** O(V)。

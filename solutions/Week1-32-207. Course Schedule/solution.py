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

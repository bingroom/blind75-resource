# Course Schedule

- **LeetCode:** [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

有 numCourses 門課與先修關係 [a,b] 表示修 a 前需先修 b，判斷能否全部修完（即是否存在合法修課順序）。

## 思路

- **有向圖是否有環：** 建圖後用 DFS + 三色（未訪/訪問中/完成）偵環。若存在反向邊（到「訪問中」的節點）則有環，無法全部修完。

## 時間 / 空間複雜度

- **時間:** O(V+E)。
- **空間:** O(V)。

## 相關閱讀

- **演算法:** Topological Sort、Cycle Detection、DFS

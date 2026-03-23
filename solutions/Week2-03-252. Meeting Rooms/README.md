# Meeting Rooms

**Topic:** Array
- **LeetCode 連結:** [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- **難度:** Easy

## 題目描述

給定一組會議的時間區間，判斷一個人是否能參加所有會議（即所有會議之間是否沒有時間重疊）。

## 解題思路

1. 將所有會議按開始時間排序。
2. 逐一檢查相鄰的兩個會議，若後一個的開始時間早於前一個的結束時間，則有重疊。
3. 若發現重疊回傳 false，否則全部檢查完後回傳 true。

## 程式碼

```python
# LeetCode 252. Meeting Rooms
# Time: O(n log n)  Space: O(1)

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # overlap found
        return True
```

## 複雜度分析

- **時間複雜度:** O(n log n) for sorting
- **空間複雜度:** O(1) ignoring sort space

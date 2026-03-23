# Merge k Sorted Lists

**Topic:** Heap
- **LeetCode 連結:** [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- **難度:** Hard

## 題目描述

給定 k 條已排序的鏈結串列，將它們合併成一條排序的鏈結串列並回傳。

## 解題思路

1. 建立一個最小堆積（min-heap），將每條鏈結串列的頭節點放入堆積。
2. 每次從堆積中取出值最小的節點，接到結果鏈結串列的尾端。
3. 若該節點有下一個節點，將其推入堆積。
4. 重複直到堆積為空，回傳結果。

## 程式碼

```python
# LeetCode 23. Merge K Sorted Lists
# 時間複雜度: O(N log k)  N=總節點數, k=鏈表數  空間複雜度: O(k)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合併 k 條已排序鏈表。用 min-heap 存每條的頭，每次 pop 最小、接上並把該鏈下一節點 push。
        """
        dummy = ListNode(0)
        cur = dummy
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
```

## 複雜度分析

- **時間複雜度:** O(N log k)，N 為總節點數。
- **空間複雜度:** O(k)。

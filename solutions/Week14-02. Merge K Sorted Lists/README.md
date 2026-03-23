# Merge k Sorted Lists

**Topic:** Linked List

- **LeetCode:** [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

 

**Example 1:**

```

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

```

**Example 2:**

```

Input: lists = []
Output: []

```

**Example 3:**

```

Input: lists = [[]]
Output: []

```

 

**Constraints:**

	- `k == lists.length`

	- `0 <= k <= 10^4`

	- `0 <= lists[i].length <= 500`

	- `-10^4 <= lists[i][j] <= 10^4`

	- `lists[i]` is sorted in **ascending order**.

	- The sum of `lists[i].length` will not exceed `10^4`.

## Solution

```python
# LeetCode 23. Merge K Sorted Lists
# 時間複雜度: O(N log k)  N=總節點數, k=鏈表數  空間複雜度: O(k)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

## 思路

- **Min-Heap：** 把每條鏈表的頭節點放入 heap，每次 pop 最小值接到結果鏈表，並把該節點的 next（若有）push 進 heap。需在 heap 中加索引以處理同值比較。

## 時間 / 空間複雜度

- **時間:** O(N log k)，N 為總節點數。
- **空間:** O(k)。

## 相關閱讀

- **資料結構:** Heap、Linked List
- **演算法:** K-way Merge

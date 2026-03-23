# Min Stack

**Topic:** Stack
- **LeetCode 連結:** [155. Min Stack](https://leetcode.com/problems/min-stack/)
- **難度:** Medium

## 題目描述

設計一個支援 push、pop、top 以及在常數時間內取得最小值的堆疊。每次操作都必須是 O(1) 時間複雜度。

## 解題思路

1. 使用一個堆疊，每個元素存為 (值, 當前最小值) 的配對。
2. push 時，比較新值與堆疊頂端的最小值，取較小者作為新的當前最小值。
3. pop 直接移除頂端元素，top 回傳頂端的值，getMin 回傳頂端的最小值。

## 程式碼

```python
# LC 155. Min Stack (Medium)
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []      # stores (value, current_min) pairs

    def push(self, val: int) -> None:
        cur_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

## 複雜度分析

- **時間複雜度:** O(1) for all operations
- **空間複雜度:** O(n)

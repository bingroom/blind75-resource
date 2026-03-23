# Implement Queue using Stacks

**Topic:** Stack
- **LeetCode 連結:** [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- **難度:** Easy

## 題目描述

僅使用兩個堆疊（stack）來實作一個先進先出（FIFO）的佇列（queue），支援 `push`、`pop`、`peek` 和 `empty` 操作。

## 解題思路

1. 使用兩個堆疊：`in_stack` 負責接收新元素，`out_stack` 負責輸出元素。
2. `push` 操作直接將元素推入 `in_stack`。
3. `pop` 或 `peek` 時，若 `out_stack` 為空，則將 `in_stack` 中所有元素逐一彈出並推入 `out_stack`（順序反轉）。
4. 從 `out_stack` 頂端取出元素，即為佇列的最前端元素。此方法使每個元素最多被搬移一次，均攤時間為 O(1)。

## 程式碼

```python
# LC 232. Implement Queue using Stacks (Easy)
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.in_stack = []   # for push
        self.out_stack = []  # for pop/peek

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        """Transfer elements from in_stack to out_stack only when out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

## 複雜度分析

- **時間複雜度:** O(1) amortized per operation
- **空間複雜度:** O(n)

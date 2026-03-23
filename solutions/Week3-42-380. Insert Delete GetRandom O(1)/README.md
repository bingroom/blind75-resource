# Insert Delete GetRandom O(1)

**Topic:** Hash Table
- **LeetCode 連結:** [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
- **難度:** Medium

## 題目描述

設計一個資料結構，支援 O(1) 時間的插入、刪除和隨機取值操作。

## 解題思路

1. 結合陣列和雜湊表：陣列儲存值，雜湊表記錄值到索引的映射。
2. 插入時在陣列末尾加入，更新雜湊表。
3. 刪除時將目標元素與陣列最後一個元素交換，然後移除最後一個元素並更新雜湊表。
4. 隨機取值時從陣列中隨機選取。

## 程式碼

```python
# LeetCode 380. Insert Delete GetRandom O(1)
# Time: O(1) per operation  Space: O(n)

import random


class RandomizedSet:
    """
    Combine a list (for O(1) random access) with a hash map
    (val -> index) for O(1) insert and delete.
    To remove in O(1): swap the target with the last element, then pop.
    """

    def __init__(self):
        self.vals = []           # stores values in arbitrary order
        self.val_to_idx = {}     # value -> index in self.vals

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        # Move last element into the slot of the removed element
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        # Remove the last element
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
```

## 複雜度分析

- **時間複雜度:** O(1) average per `insert`, `remove`, and `getRandom`.
- **空間複雜度:** O(n) where n is the number of elements in the set.

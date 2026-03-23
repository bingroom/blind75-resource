# Maximum Frequency Stack

**Topic:** Stack
- **LeetCode 連結:** [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)
- **難度:** Hard

## 題目描述

設計一個最大頻率堆疊，支援 push 和 pop 操作。pop 時移除並回傳堆疊中出現頻率最高的元素；若頻率相同，則移除最近加入的那個。

## 解題思路

1. 維護一個頻率表（val -> 當前頻率）和分組表（頻率 -> 堆疊）。
2. push 時將元素的頻率加 1，並將其加入對應頻率的堆疊，同時更新最大頻率。
3. pop 時從最大頻率的堆疊中彈出元素，將該元素的頻率減 1。
4. 若該頻率的堆疊變空，將最大頻率減 1。

## 程式碼

```python
# LC 895. Maximum Frequency Stack (Hard)
# https://leetcode.com/problems/maximum-frequency-stack/

from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)        # val -> current frequency
        self.group = defaultdict(list)      # frequency -> stack of values at that freq
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        # Pop from the most frequent group
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        # If this frequency group is now empty, decrease max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
```

## 複雜度分析

- **時間複雜度:** O(1) for both push and pop
- **空間複雜度:** O(n)

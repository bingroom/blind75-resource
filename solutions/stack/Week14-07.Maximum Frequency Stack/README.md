# Maximum Frequency Stack

## Problem Description
Design a stack-like data structure where `push` adds an element and `pop` removes the most frequent element. If there is a tie in frequency, the element closest to the top (most recently pushed) is removed.


## Solution

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

## Approach
Maintain two mappings: `freq` maps each value to its current frequency, and `group` maps each frequency level to a stack of values pushed at that frequency. Track `max_freq`. On `push`, increment the value's frequency and append it to `group[new_freq]`. On `pop`, pop from `group[max_freq]`, decrement the value's frequency, and if that group becomes empty, decrement `max_freq`. This works because a value with frequency f appears in groups 1 through f, so decrementing preserves consistency.

## Complexity
- **Time:** O(1) for both push and pop
- **Space:** O(n)

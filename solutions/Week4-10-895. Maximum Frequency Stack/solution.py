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

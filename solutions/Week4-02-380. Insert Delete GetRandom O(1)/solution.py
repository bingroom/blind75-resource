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

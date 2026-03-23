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
